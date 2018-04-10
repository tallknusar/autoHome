#!/usr/bin/python

import paho.mqtt.client as paho
#import paho.mqtt.subscribe as subscribe
 
class subscribe:
	host = ""
	topic = ""

	def __init__(self,host,topic,setter,status,client_id,port,authDict):
			self.host = host
			self.topic = topic
			self.setter = setter
			self.status = status
			self.client_id = client_id
			self.port = port
			self.authDict = authDict
			#status.publish("Made new subscriber")
			print("Made new subscriber")

	

	def run(self):



		
		def on_subscribe(self,client, userdata, mid, granted_qos):
			self.status.publish(("Subscribed to : " + self.topic))
			print("Subscribed to : " + self.topic)
	 
		def on_message(client, userdata, msg):
			
			setSet(msg.payload)  
		
		def setSet(payload): 
			self.setter.setSetpoint(int(payload.decode("utf-8")))
		
			
		client = paho.Client()
		client.on_subscribe = on_subscribe
		client.on_message = on_message
		client.connect(self.host, self.port)
		client.username_pw_set(self.authDict['username'],self.authDict['password'])
		client.subscribe(self.topic, qos=1)
	 
		client.loop_forever()
		
	