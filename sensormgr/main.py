#!/usr/bin/python

from __future__ import print_function

import os
import sys
import argparse
import time
import yaml

from stevedore import driver, enabled


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--sensors', '-s',
                   default='sensors.yml')
    return p.parse_args()


def check_enable(ex):
    return ex.plugin.should_enable()

def main():
    args = parse_args()

    mgr = enabled.EnabledExtensionManager(
        namespace='sensormgr.drivers',
        check_func = check_enable,
        invoke_on_load=False,
    )

    print('Available drivers:', mgr.names())

    with open(args.sensors) as fd:
        config = yaml.load(fd)

    sensors = []
    for spec in config['sensors']:
        if spec['method'] not in mgr.names():
            print('skipping %(name)s: no driver available for method '
                  '%(method)s.' % spec)
            continue

        sensor = mgr[spec['method']].plugin(spec)
        sensors.append(sensor)

    while True:
        for sensor in sensors:
            print('%s: %s' % (
                sensor.cfg['name'],
                sensor.sense()))
        time.sleep(5)


if __name__ == '__main__':
    main()


