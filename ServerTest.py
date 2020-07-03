#Senior Project - Cebrin Billings
#ZPPS: Zombie Plant Prevention System

#Test module

# Library Imports
from gpiozero import LED
from time import sleep

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)