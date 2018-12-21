#!/usr/bin/python3

from pyHS100 import SmartPlug
import dht
import time
import threading
import status

#termostat for styring av ovner

class Termostat():
	#initial setpoint
	setpoint = 20
	def __init__(self,deviceList):
		self.deviceList = deviceList


	def setSetpoint(self,set):
		self.setpoint = set
		status.publish("192.168.1.1",("New SetPoint: " + str(set)))
		print("New SetPoint: " + str(set))

	
			


	def run(self):
		on = None
		testBuff = 0
		flag = 1
		while(True):
			
			
			#*********DIAG*******
			testTemp = dht.getTemperature()	
			
			#********************





			if (testTemp < self.setpoint  and on != True):
				status.publish("localhost",str(on)+"" + str(testTemp))
				self.deviceList.getObject("varmeKjokken").turn_on()
				self.deviceList.getObject("varmeStue").turn_on()
				self.deviceList.getObject("varmeOlje").turn_on()
				print("Heat On!")
				status.publish("localhost","Heat ON! " +
				 '{0:0.1f}'.format(testTemp) + "C")
				on = True

			elif(testTemp >= self.setpoint +1 and on != False):
				status.publish("localhost",str(on)+ "" + str(testTemp))
				self.deviceList.getObject("varmeKjokken").turn_off()
				self.deviceList.getObject("varmeStue").turn_off()
				self.deviceList.getObject("varmeOlje").turn_off()
				status.publish("localhost",("Heat OFF! "
				 + '{0:0.1f}'.format(testTemp)+ "C" ))
				print("Heat Off!")
				on = False
			
			testBuff = testTemp
			flag = 0	