#!/usr/bin/python3

import paho.mqtt.subscribe as subscribe
host = 'm23.cloudmqtt.com'
port = 14558
client_id = 'pyBox'
authDict={'username':"czoozdoy",'password':"6tXhiKAv6LTI"}

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

subscribe.callback(on_message_print, "set" ,hostname = host, port = port, client_id=client_id,auth=authDict)