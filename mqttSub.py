#!/usr/bin/python

import paho.mqtt.client as paho
import status
 
class subscribe:
	host = ""
	topic = ""

	def __init__(self,host,topic,setter):
			self.host = host
			self.topic = topic
			self.setter = setter
			status.publish("localhost","Made new subscriber")
			print("Made new subscriber")

	def run(self):

		
		def on_subscribe(client, userdata, mid, granted_qos):
			status.publish(self.host,("Subscribed to : " + self.topic))
			print("Subscribed to : " + self.topic)
	 
		def on_message(client, userdata, msg):
			
			setSet(msg.payload)  

		def setSet(payload): 
			self.setter.setSetpoint(int(payload.decode("utf-8")))
		

		client = paho.Client()
		client.on_subscribe = on_subscribe
		client.on_message = on_message
		client.connect(self.host, 1883)
		client.subscribe(self.topic, qos=1)
	 
		client.loop_forever()

#Main()	