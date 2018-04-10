#!/usr/bin/python3
import device

from pyHS100 import SmartPlug
pluggObject = SmartPlug("192.168.1.178")
plugg1 = device.Device("plugg1","localhost", pluggObject)

plugg1.getStatus()