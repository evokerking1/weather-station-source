import bme280 # Import the BME280 module
import smbus2 # Import the SMBus module of the I2C library
from time import sleep # Import the sleep function from the time module


# Create the BME280 sensor object


port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

while True:
    bme280_data = bme280.sample(bus, address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)
