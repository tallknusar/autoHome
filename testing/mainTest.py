#!/usr/bin/python3
from pyHS100 import Discover
import device


host = "localhost"

from pyHS100 import Discover
deviceList = []

for dev in Discover.discover().values():
    #tempName = dev.sys_info['alias']
    #dev.sys_info['alias'] = device.Device(host,dev)
    #print(dev.sys_info['alias'])
    deviceList.append(device.Device(host,dev))
    #print("%s" %dev.hw_info)
    #print(dev)
#print(len(deviceList))

def getObjcet(object):
    for dev in deviceList:
        if(dev.getObject().sys_info['alias'] == object):
            return dev



VarmeKjokken = getObjcet("VarmeKjokken")
'''
i = 0

while(i < len(deviceList)):
    deviceList[i].getFullStatus()
    i += 1
'''    