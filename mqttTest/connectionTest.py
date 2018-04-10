#!/usr/bin/python3

import status

authDict={'username':"czoozdoy",'password':"6tXhiKAv6LTI"}

mtest = status.Message('m23.cloudmqtt.com','14558','ramdom',authDict)

mtest.publish()

