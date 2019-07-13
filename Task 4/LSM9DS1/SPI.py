import board
import busio
from digitalio import DigitalInOut, Direction

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
csag = DigitalInOut(board.D5)
csag.direction = Direction.OUTPUT
csag.value = True
csm = DigitalInOut(board.D6)
csm.direction = Direction.OUTPUT
csm.value = True

sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

sensor.accel_range = adafruit_lsm9ds1.ACCELRANGE_4G
sensor.mag_gain = adafruit_lsm9ds1.MAGGAIN_8GAUSS
sensor.gyro_scale = adafruit_lsm9ds1.GYROSCALE_500DP

while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(accel_x, accel_y, accel_z))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(mag_x, mag_y, mag_z))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    print('Temperature: {0:0.3f}C'.format(temp))
    # Delay for a second.
    time.sleep(1.0)