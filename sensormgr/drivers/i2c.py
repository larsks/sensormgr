from __future__ import absolute_import

import os

from .base import Driver

class I2CSensor (Driver):
    def sense(self):
        return 1

    def set(self, val):
        pass

    @classmethod
    def should_enable(cls):
        return os.path.exists('/dev/i2c-0')
