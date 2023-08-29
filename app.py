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
tx_hash = contract.constructor().transact()

# Get tx receipt to get contract address
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Deployed Contract instance
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi, )

#Control Interface
for i in pinList:
    print(i, 'Pin Status: {}' .format(contract_instance.functions.pinStatus(i).call()))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/<pin_id>/<action>")
def set_pin_status(pin_id, action):
    #Actuator configuration
    if pin_id=='fourteen':
        pin_number=14
    elif pin_id=='fifteen':
        pin_number=15
    elif pin_id=='eighteen':
        pin_number=18
    elif pin_id=='twentythree':
        pin_number=23
    elif pin_id=='twentyfour':
        pin_number=24
    elif pin_id=='twentyfive':
        pin_number=25
    elif pin_id=='eight':
        pin_number=8
    elif pin_id=='seven':
        pin_number=7
    elif pin_id=='twelve':
        pin_number=12
    elif pin_id=='sixteen':
        pin_number=16
    elif pin_id=='twenty':
        pin_number=20
    elif pin_id=='twentyone':
        pin_number=21
    elif pin_id=='two':
        pin_number=2
    elif pin_id=='three':
        pin_number=3
    elif pin_id=='four':
        pin_number=4
    elif pin_id=='seventeen':
        pin_number=17
    elif pin_id=='twentyseven':
        pin_number=27
    elif pin_id=='twentytwo':
        pin_number=22
    elif pin_id=='ten':
        pin_number=10
    elif pin_id=='nine':
        pin_number=9
    elif pin_id=='eleven':
        pin_number=11
    elif pin_id=='five':
        pin_number=5
    elif pin_id=='six':
        pin_number=6
    elif pin_id=='thirteen':
        pin_number=13
    elif pin_id=='nineteen':
        pin_number=19
    elif pin_id=='twentysix':
        pin_number=26
    else:
        return render_template('index.html')

    #Control interface
    if action=='on':
         pin_status = 1
    else:
        pin_status = 0
    tx_hash = contract_instance.functions.setPinStatus(pin_number, pin_status).transact({'from': w3.eth.accounts[0]})
    print('Transaction submitted:', tx_hash.hex())
    pin_status = format(contract_instance.functions.pinStatus(pin_number).call())
    print(f'Pin {pin_number} status changed to {pin_status}')
    if pin_status == "1":
        GPIO.output(pin_number,GPIO.HIGH)
    else:
        GPIO.output(pin_number,GPIO.LOW)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
