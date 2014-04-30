from __future__ import absolute_import

import subprocess
import shlex

from .base import Driver

class CommandSensor (Driver):
    def configure(self):
        self.command = self.cfg['command']['command']
        self.shell = self.cfg['command'].get('shell')
        if not self.shell:
            self.command = shlex.split(self.command)

    def read_value(self):
        stdout = subprocess.check_output(
            self.command, shell=self.shell)
        if self.cfg['command'].get('strip'):
            stdout = stdout.strip()
        return stdout
