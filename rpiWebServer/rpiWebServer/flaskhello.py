
#helloworld program on flask
#to run use
#sudo python3 flaskhello.py
#check output on your rpi link for eg. 192.168.1.114
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello from flask server!!☺️'
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
