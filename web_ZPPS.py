from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os
from time import sleep

app = Flask(__name__)



def template(title = "Welcome to ZPPS", sensors = ["","","",""]):
    recentSensor = water.get_last_measured()
    h2o = water.get_last_watered()
    templateDate = {
        'title' : title,
        'measured' : recentSensor,
        'sensor1' : sensors[0],
        'sensor2' : sensors[1],
        'sensor3' : sensors[2],
        'sensor4' : sensors[3],
        'watered' : h2o
        }
    return templateDate

@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = [water.get_status(11), 0, 1, 2]
    list = []
    for x in status:
        if (x == 0):
            list.append("Water me please!")
        else:
            list.append("I'm a happy plant")

    templateData = template(sensors = list)
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

@app.route("/autowater")
def water_timed():
    print ("Here we go! Press CTRL+C to exit")
    try:
        water.pump_on()
        sleep(900)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        water.pump_off()
        GPIO.cleanup() # cleanup all GPI
    
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
    app.run(host='0.0.0.0', port=80, debug=True)