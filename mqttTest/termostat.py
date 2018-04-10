#!/usr/bin/python3

from pyHS100 import SmartPlug
import dht
import time
import threading


#termostat for styring av ovner

class Termostat():
	#initial setpoint
	setpoint = 23
	def __init__(self,deviceList,status):
		self.deviceList = deviceList
		self.status = status

	def setSetpoint(self,set):
		self.setpoint = set
		status.publish(("New SetPoint: " + str(set)))
		print("New SetPoint: " + str(set))

	def getSetpoint(self):
		return self.setpoint

	def run(self):
		on = None
		while(True):

			
			if (dht.getTemperature() < self.setpoint  and (on != True or on == None)):
				self.deviceList.getObject("VarmeKjokken").turn_on()
				self.deviceList.getObject("VarmeStue").turn_on()
				print("Heat On!")
				print(dht.getTemperature())
				self.status.publish("Heat ON! " + '{0:0.1f}'.format(dht.getTemperature()) + "C" + " Setpoint: " + str(self.setpoint))
				on = True

			elif(dht.getTemperature() > self.setpoint +1 and (on != False or on == None)):
				self.deviceList.getObject("VarmeKjokken").turn_off()
				self.deviceList.getObject("VarmeStue").turn_off()
				self.status.publish(("Heat OFF! " + '{0:0.1f}'.format(dht.getTemperature())+ "C" + " Setpoint: " + str(self.setpoint)))
				print("Heat Off!")
				print(dht.getTemperature())
				on = False