# Basic Settings
import RPi.GPIO as GPIO
import time
import spidev
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Temp, Humid Settings(DHT11) - 26
import Adafruit_DHT
DHT_sensor = Adafruit_DHT.DHT11
DHT_Pin = 26

# LED Settings - R 17, Y 27, G 22
RED_LED_Pin = 17
YELLOW_LED_Pin = 27
GREEN_LED_Pin = 22
GPIO.setup(RED_LED_Pin, GPIO.OUT)
GPIO.setup(YELLOW_LED_Pin, GPIO.OUT)
GPIO.setup(GREEN_LED_Pin, GPIO.OUT)

# Gas Sensor Settings(MQ2_Digital_Mode) - 16
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000

def analog_read(channel):
  r = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((r[1]&3) << 8) + r[2]
  return adc_out

# Gas Sensor Settings(MQ2_Digital_Mode) - 23
Fire_Pin = 23
GPIO.setup(Fire_Pin, GPIO.IN)


#####################    MAIN CODE   #######################
# 4ossil Test Code

h, t = Adafruit_DHT.read_retry(DHT_sensor, DHT_Pin)

if(GPIO.input(Fire_Pin))==True:
    f=1
else:
    f=0

g = analog_read(0) * 3.3
if g<100:
    g=100.0

    
if t is not None and h is not None and f is not None and g is not None:
    print t,',',h,',',f,',',g
else:
    print ('Read Error')
