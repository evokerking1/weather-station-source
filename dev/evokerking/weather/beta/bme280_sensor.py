import bme280 # Import the BME280 module
import smbus2 # Import the SMBus module of the I2C library


# Create the BME280 sensor object

class sensor.bme280{
    def init ():
        port = 1
        address = 0x77 # Adafruit BME280 address. Other BME280s may be different
        bus = smbus2.SMBus(port)
        bme280.load_calibration_params(bus, address)
        
    
    

    def get.all():
        bme280_data = bme280.sample(bus, address)
        humidity  = bme280_data.humidity
        pressure  = bme280_data.pressure
        ambient_temperature = bme280_data.temperature
        print(humidity, pressure, ambient_temperature)
        return humidity, pressure, ambient_temperature

    def get.humidity():
        bme280_data = bme280.sample(bus, address)
        humidity = bme280.sample
}
