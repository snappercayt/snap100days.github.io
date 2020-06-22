# Welcome to snapp100days
[this](https://snappercayt.github.io/snapp100days/) is where I will be posting blogs for the next 100 days 


## Day 1
### 19th april 2020

1. history of [webassembly](https://www.youtube.com/watch?v=6r0NKEQqkz0)
2. android webview 101 [check this youtube video](https://www.youtube.com/watch?v=qMvbtcbEkDU) 
3. analog linux iio  [to read from ADC](https://wiki.analog.com/software/linux/docs/iio/iio)
4. what's new in chrome 81 [another video](https://www.youtube.com/watch?v=ihjL0mcnlQs)
5. interact with NFC from the [web](https://web.dev/nfc/)
6. ndef for dummies [a new file format](https://www.dummies.com/consumer-electronics/nfc-data-exchange-format-ndef/)
7. pubg on pixelbook [because its a new platform](https://www.youtube.com/watch?v=kh_1IBGWG_8)


## Day 2
### 20th april 2020
1. a library in python to interface R307 fingerprint sensor [pyfingerprint](https://github.com/bastianraschke/pyfingerprint)
2. You may need to run processes in your python based application to get work done [use this](https://docs.python.org/3/library/subprocess.html#subprocess.run)
3. to add arguments to processes, more [docs](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments) and some [example](http://queirozf.com/entries/python-3-subprocess-examples) on that 


## Day 3
### 24th april 2020
1. using python trees and [recursion](https://www.youtube.com/watch?v=7tCNu4CnjVc) with computerphyle, did my own edits too 
2. leetcode [problems](https://leetcode.com/problems/minimum-number-of-frogs-croaking/submissions/)
3. docker [tutorial](https://www.youtube.com/watch?v=eGz9DS-aIeY)


## Day 4
### May 3rd 2020

1. found this cool paper which Luca DellAnna talks about, using humain brain cortex model to derive context 
from pattern maching and lot more for the data available, [clickhere](https://luca-dellanna.com/wp-content/uploads/2019/01/Techniques-for-the-Emergence-of-Meaning-in-ML.pdf)
2. revolution was some thing that was trending in 2015 [gpgpu library for raspberrypi](https://github.com/hermanhermitage/videocoreiv)
3. decided to work on some dapps because that is what one twitter follower suggest so started reading about that
[a blog on dapps with examples](https://hackernoon.com/what-are-decentralized-applications-dapps-explained-with-examples-7ff8f2c4a460)
4. found this interesting software to scale images to 4k using DLNN [Waifu2x isa awesome](https://github.com/AaronFeng753/Waifu2x-Extension-GUI)
5. answered some stack overflow question and that peeked my interest in pandas again [check here](https://stackoverflow.com/users/11679090/snappercayt)

## Day 5
### May 5th 2020

1. sqlite database to flask using SLQAlchemy is [cool](https://www.sqlitetutorial.net/) and uses so less space
2. converting a html page to flask compatible html is difficult
3. IEX cloud python SDK for free tier is garbage, paid works better
4. other HTML pages in flask are kept in templates folder, while in JS its kept in assets
5. startnig from scratch makes you cover more ground than using premade code if you are not sure about it refer, buying program is not a good choice
6. make a web scraper that screens off, HTML, assets, JS all in one program
7. cookiecutter can be used to create a [python package](https://github.com/cookiecutter/cookiecutter)
8. bootstrap makes basic HTML [cool](https://designmodo.com/bootstrap-5/)
9. deploying a python app to AWS seems [easy](https://www.freecodecamp.org/news/how-to-create-auto-updating-data-visualizations-in-python-with-matplotlib-and-aws/)
10. pyqt5 can be used to browse websites [check this video](https://www.youtube.com/watch?v=atn0zb3TRY8)

## Day 4
### May 8th 2020

1. i added my LoginManger before from app import routes, models and it worked. If you want to have some route to something then it has to be there before you create a LoginManager
2. While copying code always look at the minutest bits  
3. [this](https://i.imgur.com/XIFhwew.png) code gave me lot of headache, I had done a typo when I was writing this join code where I added join to the same coloumn i.e. 


```
#both join to follower_id
primaryjoin=(followers.c.follower_id == id),
secondaryjoin=(followers.c.follower_id == id)

#instead of the correct version given below where both have 
#different names, follower_id and followed_id
primaryjoin=(followers.c.follower_id == id),
secondaryjoin=(followers.c.followed_id == id),
```
4. the way this tutorial is coded and brought to life, [virtual graphics](
https://youtu.be/PahbNFypubE) never stop amazing me



## Day 5
### May 11th 2020
1. version control is very important for software development, GIT is the most widely used version control method. This Stanford document covers all the basics and working of [GIT](https://missing.csail.mit.edu/2020/version-control/)
2. a purpose build software intelligence platform for [enterprise cloud](https://www.dynatrace.com/support/help/get-started/what-is-dynatrace/)
3. automate simple tasks on android phone using this cool [app](https://llamalab.com/automate/)
4. an open source software for OCR, [guide by NYU](https://guides.nyu.edu/tesseract)
5. alternate firmware for configuration for ESP8266 based devices with options for webUI, OTA updates, automation using timers or rules, expandability and entirely local control over MQTT, HTTP, Serial or KNX. [check this github link](https://github.com/arendst/Tasmota)
6. 


## Day 6
### May 22th 2020
1. Learnt how to make a desktop shortcut of any application on Ubuntu 18.04 LTS using [this link](https://linuxconfig.org/how-to-create-desktop-shortcut-launcher-on-ubuntu-18-04-bionic-beaver-linux) gtk is cool!
2. Learnt installing anything on Ubuntu or linux is better to use a terminal based package manager like apt-get or snap to install developer tools eg. pycharm 
3. It is possible to use a physical device to be used for developement of an app, to build and debug an android app by using adb wifi plugin to android studio
4. Have to try flutter to build a simple app, also have to check how to remove that error on pyfingerprint module, have to try more examples of node-red, have to study [this](https://www.hindawi.com/journals/wcmc/2018/7470234/) and understand how to use raspberrypi cluster for understanding cloud and deploying servers on it, have to find a way to send raspberrypi data over internet to a developement server I choose 🤔
5. Here is a java based demo to create fractals using Ray-marching check [this link](https://github.com/tatiana-s/mandelbulb-renderer)
### Update 
I have been busy with understanding graphics created with best way to utilize best methods like [Ray Marching](https://www.youtube.com/watch?v=Cp5WWtMoeKg), understood why computation is cheap but fetching bytes from DRAM is expensive in terms of energy for GPUs, having fun looking at [fractals](https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/f/Fractal.htm), also trying to understand if we can make raspberry pi 4 cluster and deploy a web server on it over a kubernetes layer, in the day was busy setting up the LAMP stack using mysql-server , pycharm-community , android studio using IntelliJ IDEA

## Day 7
### May 24th 2020
what if its possible to create a bot(a twitter bot preferably) to which you can tag some image(like some qr code or link to something) which then converts that image into a fractal image and sends it you, this said fractal image will be made using the thing you tagged it with, and I hope this can be used your secure key of your choice whatever it maybe, just brain dump 

1. python bluetooth libraries on windows are tough to work with eg. bluetool 
2. installing php using XAMPP on windows is the best way to setup LAMP stack on windows distribution, bitnami has modules for wordpress to help you better manage your website later
3. adb or Android Debug Bridge can sometimes not work with windows for few reasons
   * driver of the Android device connected to the USB of the computer might be outdated
   * the adb service might need restart if the device is not detected
4. need to find a way to change the font of the title bar menu of python tkinter
5. also need to find libararies to make bluetooth and wifi communication possible on python 

## Day 8
### June 18th 2020
1. installing kivy is not so simple read documentation carefully [for rpi](https://kivy.org/doc/stable/installation/installation-rpi.html) and [for windows](https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist)

## Day 9
### June 22nd 2020
1. had a curiosity about what does Whatsapp use for messaging and stumbled onto [ejabberd.im](https://ejabberd.im/) its a server that does a lot of things and does one most important thing creates a XMPP server basically. 
2. Now, once you can make your own server and set it up wherever you want(do not use AWS omg i wasted 2 hours on it as it is so not easy and there is no simple tutorial on it as I was trying to install openfire which is a type of XMPP server and that is not the same as ejabberd UGGHHHH 😭😭😭) So I am still trying to use AWS till they don't charge me anythin
3. We also need a client to let anyone connec to the group on the XMPP server and chat! that is where this open source chat app [conversatoins](https://f-droid.org/en/packages/eu.siacs.conversations/) comes into picture
4. Also installing wordpress on windows machine using XAMPP is not really easy if you haven't done it before 
