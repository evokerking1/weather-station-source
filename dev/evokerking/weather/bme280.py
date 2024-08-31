
# Create the BME280 sensor object
import bme280
import smbus2
from time import sleep

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)
