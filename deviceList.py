#!/usr/bin/python3

from pyHS100 import Discover
import mqttDevice
import status
import paho.mqtt.publish as publish

#Finner enheter på nettverket, lager mqttDevice Objekt. Legger inn i
#deviceList


class devList:
	deviceList = []
	def __init__(self,host):
		self.host = host
		for dev in Discover.discover().values():
    
			self.deviceList.append(mqttDevice.Device(self.host,dev))

		print("Made new device with " +str(len(self.deviceList)) + " devices")	
		#status.publish("localhost","status",("Made new list with " +str(len(self.deviceList)) + " devices"))
		
#Tar inn navn på device(String), sammeligner med navn i listen og returnerer mqttDevice objektet
#TODO: bytte for loop

	def getObject(self,deviceName):
		#print("Looking for " + deviceName + " in the device list")
		i = 0
		while( i < len(self.deviceList)):
			if(self.deviceList[i].getObject().sys_info['alias'] == deviceName):
				#print("Returning device " + self.deviceList[i].getObject().sys_info['alias'])
				#status.publish("localhost","status",("Returning device " + self.deviceList[i].getObject().sys_info['alias']))
				return self.deviceList[i].getObject()

			
			i +=1
