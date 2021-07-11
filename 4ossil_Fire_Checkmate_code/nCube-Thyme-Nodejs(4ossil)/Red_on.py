# Basic Settings
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# LED Settings - R 17, Y 27, G 22
RED_LED_Pin = 17
YELLOW_LED_Pin = 27
GREEN_LED_Pin = 22
GPIO.setup(RED_LED_Pin, GPIO.OUT)
GPIO.setup(YELLOW_LED_Pin, GPIO.OUT)
GPIO.setup(GREEN_LED_Pin, GPIO.OUT)

GPIO.output(RED_LED_Pin, GPIO.LOW)
GPIO.output(YELLOW_LED_Pin, GPIO.LOW)
GPIO.output(GREEN_LED_Pin, GPIO.LOW)


GPIO.output(RED_LED_Pin, GPIO.HIGH)