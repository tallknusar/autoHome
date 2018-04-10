#!/usr/bin/python

import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def getTemperature():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	#print(temperature)
	if temperature is not None:

		return temperature

	else:
	
		return('Error!')	


def getHumidity():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None:

		return humidity

	else:
	
		return('Error!')
