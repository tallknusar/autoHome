#!/usr/bin/python3

import threading
import termostat
import deviceList
import mqttSub
import dhtMqttPublisher
import paho.mqtt.publish as publish
import status
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('autoHOME'))

host = "localhost"
devices = deviceList.devList(host)
termo = termostat.Termostat(devices)
tempSet = mqttSub.subscribe(host,"temperature/set",termo)
dhtPub = dhtMqttPublisher.pub(host,"temperature")

threading.Thread(target=termo.run).start()
threading.Thread(target=tempSet.run).start()
threading.Thread(target=dhtPub.run).start()

