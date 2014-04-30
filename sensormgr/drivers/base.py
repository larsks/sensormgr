from six import with_metaclass
from dogpile.cache import make_region

default_cache_lifetime = 60


class CacheMeta (type):
    def __init__(cls, name, bases, attrs):
        cls.cache = make_region().configure(
            'dogpile.cache.memory',
            expiration_time=getattr(cls, 'cache_lifetime',
                                    default_cache_lifetime),
        )


class Driver (with_metaclass(CacheMeta)):
    api_version = 1
    cache_lifetime = 10

    def __init__(self, cfg):
        self.cfg = cfg
        self.configure()

    def configure(self):
        pass

    @classmethod
    def should_enable(cls):
        return True

    @property
    def cachekey(self):
        return '%s.%s.%s' % (
            self.api_version,
            self.__class__.__name__,
            self.cfg.get('name', id(self)))

    def sense(self):
        return self.cache.get_or_create(
            self.cachekey,
            self.read_value,
            expiration_time=self.cfg.get('lifetime'))

    def set(self, value):
        self.cache.delete(self.cachekey)
        self.write_value(value)

    def read_value(self):
        raise NotImplementedError()

    def write_value(self, value):
        raise NotImplementedError()
