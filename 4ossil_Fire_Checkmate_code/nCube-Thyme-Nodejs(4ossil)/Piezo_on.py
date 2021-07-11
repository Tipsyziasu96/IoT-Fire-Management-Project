# Basic Settings
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Piezo Settings - 12
Piezo_Pin = 12
GPIO.setup(Piezo_Pin, GPIO.OUT)
p = GPIO.PWM(Piezo_Pin, 523)

p.start(100)
time.sleep(8)

