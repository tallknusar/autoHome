#!/usr/bin/python3

from pyHS100 import SmartPlug
import dht
import time
import threading
import status

#termostat for styring av ovner

class Termostat():
	#initial setpoint
	setpoint = 22
	def __init__(self,deviceList):
		self.deviceList = deviceList


	def setSetpoint(self,set):
		self.setpoint = set
		status.publish("localhost",("New SetPoint: " + str(set)))
		print("New SetPoint: " + str(set))


	def run(self):
		on = None
		while(True):

			
			if (dht.getTemperature() < self.setpoint  and on != True):
				status.publish("localhost",str(on) + str(dht.getTemperature()))
				self.deviceList.getObject("VarmeKjokken").turn_on()
				self.deviceList.getObject("VarmeStue").turn_on()
				print("Heat On!")
				status.publish("localhost","Heat ON! " +
				 '{0:0.1f}'.format(dht.getTemperature()) + "C")
				on = True

			elif(dht.getTemperature() > self.setpoint +1 and on != False):
				status.publish("localhost",str(on) + str(dht.getTemperature()))
				self.deviceList.getObject("VarmeKjokken").turn_off()
				self.deviceList.getObject("VarmeStue").turn_off()
				status.publish("localhost",("Heat OFF! "
				 + '{0:0.1f}'.format(dht.getTemperature())+ "C" ))
				print("Heat Off!")
				on = False