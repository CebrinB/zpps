from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os

app = Flask(__name__)

def template(title = "ZPPS - Zombie Plant Prevention System", text = ""):
    now = datetime.datetime.now()
    record = check_last_watered()
    print (record)
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text,
        'sensor1' : "",
        'sensor2' : "",
        'sensor3' : "",
        'sensor4' : "",
        'watered' : ""
        }
    
    return templateDate

@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/last_watered")
def check_last_watered():
    templateData = template(watered = water.get_last_watered())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "I'm a happy plant!"
    else:
        message = "Water me please! "
        
    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2():
    water.pump_on()
    templateData = template(text = "Watered Once")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        templateData = template(text = "Auto Watering On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "Already running")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.4 auto_water.py&")
    else:
        templateData = template(text = "Auto Watering Off")
        os.system("pkill -f water.py")
        
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    