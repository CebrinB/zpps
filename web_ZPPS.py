from flask import Flask, render_template, redirect, url_for, request, jsonify
import urllib2
import re
import datetime
import water
import psutil
import os
from time import sleep

app = Flask(__name__)

input_pins = [11, 12, 13, 15]
output_pins = [16, 18]
list = ['','','','']

def setup_gpio():
    for x in input_pins:
        water.init_input(x)
        
    for x in output_pins:
        water.init_output(x)

def template(title = "Welcome to ZPPS"):
    recentSensor = water.get_last_measured()
    h2o = water.get_last_watered()
    valve = water.get_valve(output_pins[0])
    templateData = {
        'title' : title,
        'measured' : recentSensor,        
        'sensor1' : list[0],
        'sensor2' : list[1],
        'sensor3' : list[2],
        'sensor4' : list[3],
        'valve' : valve,
        'watered' : h2o
        }
    return templateData


@app.route("/")
def hello():        
    templateData = template()
    return render_template('main.html', **templateData)


@app.route("/sensor")
def check_soil():
    water.toggle_sensor_power(output_pins[1])
    i = 0
    for x in input_pins:
        if (water.check_soil(x)):
            list[i] = "Water me please!"
            i+=1
        else:
            list[i] = "I'm a happy plant"
            i+=1
    water.toggle_sensor_power(output_pins[1])
    templateData = template()
    return render_template('main.html', **templateData)


@app.route("/water")
def water_on():
    water.pump_on()
    templateData = template()
    return render_template('main.html', **templateData)


@app.route("/stop")
def water_off():
    water.pump_off()
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/editlabel")
def edit_label():
    
    
    templateData = template()
    return render_template('main.html', **templateData)
    

@app.route("/autowater")
def water_timed():
    print ("Here we go! Press CTRL+C to exit")
    try:
        water.pump_on()
        sleep(5)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        water.pump_off()
        water.cleanup() # cleanup all GPIO
    water.pump_off()
    templateData = template()
    return render_template('main.html', **templateData)

    
@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        #templateData = template(text = "Auto Watering On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    #templateData = template(text = "Already running")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.4 auto_water.py&")
    else:
        #templateData = template(text = "Auto Watering Off")
        os.system("pkill -f water.py")

    templateData = template()
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    setup_gpio()
    try:
        app.run(host='0.0.0.0', port=80, debug=True)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        water.cleanup() # cleanup all GPIO
    water.cleanup()