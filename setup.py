from setuptools import setup, find_packages

setup(
    name='sensormgr',
    version='1.0',

    scripts=[],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'sensormgr.drivers': [
            'gpio = sensormgr.drivers.gpio:GPIOSensor',
            'i2c = sensormgr.drivers.i2c:I2CSensor',
            'file = sensormgr.drivers.file:FileSensor',
            'command = sensormgr.drivers.command:CommandSensor',
        ],
    },

    zip_safe=False,
)

