'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
led = 19

#initialize GPIO status variables
ledSts = 0

# Define led pins as output
GPIO.setup(led, GPIO.OUT) 

# turn leds OFF 
GPIO.output(led, GPIO.LOW)
	
@app.route("/")
def index():
	# Read Sensors Status

	ledSts = GPIO.input(led)

	templateData = {
              'title' : 'GPIO output Status!',
              'led'  : ledSts,
        }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'led':
		actuator = led
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	if GPIO.input(led) == 1:
		ledSts="on 🟢"
	else:
		ledSts="off 🔴"
	
	templateData = {
              'led'  : ledSts,
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
