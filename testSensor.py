import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def get_status(pin):
    GPIO.setup(pin, GPIO.IN)
    test = GPIO.input(pin)
    print (test)
    return GPIO.input(pin)
    
def change_status(pin = 13):
    GPIO.setup(pin, GPIO.OUT)
    
    sen = GPIO.input(11)
    
    if sen:
        GPIO.output(pin, 0)
    else:
        GPIO.output(pin, 1)
    #print (GPIO.output(pin))
       
def practice():
    try:
        f = open("last_watered.txt", "r")
        eep = f.readline()
        #print (eep)
        return eep
    except:
        return "NEVER!"

print (practice())
get_status(11)
change_status()


    