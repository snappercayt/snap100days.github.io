import RPi.GPIO as GPIO
import time
import datetime
from flask import Flask, render_template

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 21
buttonSts = GPIO.LOW # we added low as default
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # here btn added as an input on pin 20

@app.route("/")
def index():
  now = datetime.datetime.now()
  timeString = now.strftime("%Y-%m-%d %H:%M")
  try:
    while True:
      buttonSts=GPIO.input(button)
      if buttonSts==False:templateData={
	    'title':'GPIO input Status!',
	    'button':buttonSts,
	    'time':timeString
	    } 
      return render_template('index.html',**templateData)   
  except:
    buttonSts=GPIO.input(button)
    templateData={
	    'title':'GPIO input Status!',
	    'button':buttonSts,
	    'time':timeString
	    } 
    return render_template('index.html',**templateData) 
    GPIO.cleanup()
    

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
