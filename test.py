import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from EmulatorGUI import GPIO
from flask import Flask
#from RPiSim import GPIO
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [14, 15, 18, 23, 24, 25, 8,7, 12, 16, 20, 21, 2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]


for i in pinList:
    GPIO.setup(i, GPIO.OUT)

app = Flask(__name__)
@app.route("/<pin>/<action>")
def control(pin, action):
    if pin=='fourteen':
        actuator=14
    if pin=='fifteen':
        actuator=15
    if pin=='eighteen':
        actuator=18
    if pin=='twentythree':
        actuator=23
    if pin=='twentyfour':
        actuator=24
    if pin=='twentyfive':
        actuator=25
    if pin=='eight':
        actuator=8
    if pin=='seven':
        actuator=7
    if pin=='twelve':
        actuator=12
    if pin=='sixteen':
        actuator=16
    if pin=='twenty':
        actuator=20
    if pin=='twentyone':
        actuator=21
    if pin=='two':
        actuator=2
    if pin=='three':
        actuator=3
    if pin=='four':
        actuator=4
    if pin=='seventeen':
        actuator=17
    if pin=='twentyseven':
        actuator=27
    if pin=='twentytwo':
        actuator=22
    if pin=='ten':
        actuator=10
    if pin=='nine':
        actuator=9
    if pin=='eleven':
        actuator=11
    if pin=='five':
        actuator=5
    if pin=='six':
        actuator=6
    if pin=='thirteen':
        actuator=13
    if pin=='nineteen':
        actuator=19
    if pin=='twentysix':
        actuator=26


    if action=='on':
         GPIO.output(actuator,GPIO.HIGH)
    if action=='off':
        GPIO.output(actuator,GPIO.LOW)
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
     
    
