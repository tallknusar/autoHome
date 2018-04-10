#!/usr/bin/python3
import dht
import paho.mqtt.publish as publish
import time

class pub:
	
	def __init__(self,host,port,client_id,authDict,topic):
		self.host = host
		self.port = port
		self.client_id = client_id
		self.authDict = authDict
		self.topic = topic	

	def run(self):
		while(True):
			publish.single(self.topic,payload = '{0:0.1f}'.format(dht.getTemperature()),qos=0,hostname = self.host, port = self.port, client_id=self.client_id,auth=self.authDict)
			#print ('{0:0.1f}'.format(dht.getTemperature()))
			time.sleep(5)