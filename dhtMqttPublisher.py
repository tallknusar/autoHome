#!/usr/bin/python3
import dht
import paho.mqtt.publish as publish
import time

class pub:
	
	def __init__(self,host,topic):
		self.host = host
		self.topic = topic		

	def run(self):
		while(True):
			publish.single(self.topic, '{0:0.1f}'.format(dht.getTemperature()), hostname=self.host)
			#print ('{0:0.1f}'.format(dht.getTemperature()))
			time.sleep(5)