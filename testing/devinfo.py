#!/usr/bin/python3

from pyHS100 import SmartDevice

device = SmartDevice("192.168.1.178")
print(device.sys_info['model'])

decive.getStatus()