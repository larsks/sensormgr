from __future__ import absolute_import

import os

from .base import Driver

class FileSensor (Driver):
    def configure(self):
        self.path = self.cfg['file']['path']

    def read_value(self):
        with open(self.path) as fd:
            data = fd.read()
            if self.cfg['file'].get('strip'):
                data = data.strip()

            return data

    def write_value(self, val):
        with open(self.path, 'w') as fd:
            fd.write(val)
