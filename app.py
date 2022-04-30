#  * SPDX-License-Identifier: MIT
#  * Licensed to @Author: Salman Dabbakuti(https://github.com/Salmandabbakuti)
#  * See the License for the specific language governing permissions and limitations under the License.

import json
from web3 import Web3, HTTPProvider
# import RPi.GPIO as GPIO # for real rasp-pi
from RPiSim.GPIO import GPIO
from flask import Flask, render_template
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [14, 15, 18, 23, 24, 25, 8,7, 12, 16, 20, 21, 2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)

# fetching abi and bytecode from artifacts file
artifacts = json.load(open('./artifacts/contracts/PinController.sol/PinController.json'))
abi = artifacts['abi']
bytecode = artifacts['bytecode']

# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:8545/"))

# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get transaction hash from deployed contract
tx_hash = contract.constructor().transact({'from': w3.eth.accounts[0], 'gas': 410000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Deployed Contract instance
contract_instance = w3.eth.contract(abi=abi, address=tx_receipt.contractAddress)

#Control Interface
for i in pinList:
    print(i, 'Pin Status: {}' .format(contract_instance.functions.pinStatus(i).call()))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/<pin>/<action>")
def control(pin, action):
    #Actuator configuration
    if pin=='fourteen':
        actuator=14
    elif pin=='fifteen':
        actuator=15
    elif pin=='eighteen':
        actuator=18
    elif pin=='twentythree':
        actuator=23
    elif pin=='twentyfour':
        actuator=24
    elif pin=='twentyfive':
        actuator=25
    elif pin=='eight':
        actuator=8
    elif pin=='seven':
        actuator=7
    elif pin=='twelve':
        actuator=12
    elif pin=='sixteen':
        actuator=16
    elif pin=='twenty':
        actuator=20
    elif pin=='twentyone':
        actuator=21
    elif pin=='two':
        actuator=2
    elif pin=='three':
        actuator=3
    elif pin=='four':
        actuator=4
    elif pin=='seventeen':
        actuator=17
    elif pin=='twentyseven':
        actuator=27
    elif pin=='twentytwo':
        actuator=22
    elif pin=='ten':
        actuator=10
    elif pin=='nine':
        actuator=9
    elif pin=='eleven':
        actuator=11
    elif pin=='five':
        actuator=5
    elif pin=='six':
        actuator=6
    elif pin=='thirteen':
        actuator=13
    elif pin=='nineteen':
        actuator=19
    elif pin=='twentysix':
        actuator=26
    else:
        return render_template('index.html')

    #Control interface
    if action=='on':
         is_active = True
    else:
        is_active = False
    tx_hash = contract_instance.functions.controlPin(actuator, is_active).transact({'from': w3.eth.accounts[0]})
    print('Transaction submitted:', tx_hash.hex())
    pin_status = format(contract_instance.functions.pinStatus(actuator).call())
    print(f'Pin {actuator} status changed to {pin_status}')
    if pin_status == 'True':
        GPIO.output(actuator,GPIO.HIGH)
    else:
        GPIO.output(actuator,GPIO.LOW)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
