#!/usr/bin/python3

import datetime
import paho.mqtt.publish as publishThis
import time

def publish(host,message):
	timedate = datetime.datetime.now().strftime("%d/%m-%y|%H:%M - ")
	publishThis.single("status",(timedate + " " + message) , hostname=host,qos=1)
	log(message)

#TODO sett inn with blokk 
def log(message):
	appendFile = open('/home/pi/autoHome/log.txt','a',newline='\n')
	timedate = datetime.datetime.now().strftime("%d/%m-%y|%H:%M:%S - ")
	appendFile.write(timedate + " " + str(message) + "\r\n")
	appendFile.close()
