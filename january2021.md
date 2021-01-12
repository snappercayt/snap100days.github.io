
# **raspberrypi server**

used this link 👇

https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d


      from flask import Flask
      app = Flask(__name__)
      @app.route('/')
      def index():
         return 'Hello from flask server!!☺️'
      if __name__ == '__main__':
         app.run(debug=True, port=80, host='0.0.0.0')

### **check rpiWebServer.zip in dowloads**

1. succesfully installed flask 
2. used flask to host a web page and display server time
3. displayed gpio value on the page
4. next, to take input from page and change board values


### **very important for linux**

      $ cat /etc/os-release


### **sample output 👇👇**

        PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
        NAME="Raspbian GNU/Linux"
        VERSION_ID="10"
        VERSION="10 (buster)"
        VERSION_CODENAME=buster
        ID=raspbian
        ID_LIKE=debian
        HOME_URL="http://www.raspbian.org/"
        SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
        BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
