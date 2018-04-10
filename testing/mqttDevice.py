#!/usr/bin/python3

import paho.mqtt.publish as publish
#from pyHS100 import SmartDevice

class Device:
	status = None

	def __init__(self,host,plug):
		
		self.host = host
		self.plug = plug
		self.status = ("%s" %self.plug.state)

	def plugOn(self):
			plug.turn_on()

	def plugOff(self):
		plug.turn_off()		

	def getStatus(self):
		print(self.plug.sys_info['model'])
		return 	self.status

	def getFullStatus(self):
		publish.single(self.plug.sys_info['alias'], "getFullStatus -> " + self.plug.sys_info['alias'] + " Status: " + str(self.status), hostname=self.host)	
