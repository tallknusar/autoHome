#!/usr/bin/python3

import datetime
import paho.mqtt.publish as publishThis

#Klasse som tar inn statusmelding og publiserer til topic "status". 


class Message:
	
	def __init__(self,host,port,client_id,authDict):
		self.host = host
		self.port = port
		self.client_id = client_id
		self.authDict = authDict

		
	def publish(self,message):
		timedate = datetime.datetime.now().strftime("%d/%m-%y|%H:%M - ")
		#publishThis.single("status",(timedate + " " + message) , hostname=host)
		try:
			publishThis.single("status",payload = timedate +
			 " " + message,qos=0,hostname = self.host, port = self.port,
			  client_id=self.client_id,auth=self.authDict)
	
		except Exception as e:
			print("Exception")
