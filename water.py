# External module imports
import RPi.GPIO as GPIO
import datetime
import time
import os

init = False

GPIO.setmode(GPIO.BOARD) # physical board pin-numbering scheme

def get_last_measured():
    try:
        f = open("last_measured.txt", "r")
        lastLine = f.readline()
        return lastLine
    except:
        return "NEVER!"
    
    
def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        lastLine = f.readline()
        return lastLine
    except:
        return "NEVER!"

    
def get_valve(pin):
    if (get_status(pin)):
        return "Closed"
    else:
        return "Open"
    get_status(pin)


def get_status(pin):
    return GPIO.input(pin)


def init_input(pin):
    GPIO.setup(pin, GPIO.IN)
    
    
def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    
    
def sensor_power_on(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def sensor_power_off(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
    
def check_soil(pin):
    f = open("last_measured.txt", "w")
    f.write("{} {}".format(datetime.datetime.today().strftime('%A'), format(datetime.datetime.now())))
    f.close()
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)

    
def auto_water(delay = 5, pump_pin = 13, water_sensor_pin = 11):
    consecutive_water_count = 0
    init_output(pump_pin)
    print ("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 0
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI
        
def pump_on(pump_pin):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Began watering: {} {}".format(datetime.datetime.today().strftime('%A'), format(datetime.datetime.now())))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    
    
def pump_off(pump_pin):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered: {} {}".format(datetime.datetime.today().strftime('%A'), format(datetime.datetime.now())))
    f.close()
    GPIO.output(pump_pin, GPIO.HIGH)
    

def cleanup():
    GPIO.cleanup()