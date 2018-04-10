#!/usr/bin/python3

import threading
import termostat
import deviceList
import mqttSub
import dhtMqttPublisher
import paho.mqtt.publish as publish
import status


host = 'm23.cloudmqtt.com'
port = 14558
client_id = 'pyBox'
authDict={'username':"czoozdoy",'password':"6tXhiKAv6LTI"}

statusMessage = status.Message(host,port,client_id,authDict)
devices = deviceList.devList(host)
termo = termostat.Termostat(devices,statusMessage)
tempSet = mqttSub.subscribe(host,"set",termo,statusMessage,
	client_id,port,authDict)
dhtPub = dhtMqttPublisher

threading.Thread(target=termo.run).start()
threading.Thread(target=tempSet.run).start()
threading.Thread(target=dhtPub.run).start()

#sudo systemctl start termostatNy.service