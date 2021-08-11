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
pinList = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)

w3 = Web3(HTTPProvider("https://testnet-rpc.gochain.io/"))
# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/homeAutomation.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
key= input("Enter your account private key with 0x prefix. We do not store it anywhere and used for this session only: ")
acct = w3.eth.account.privateKeyToAccount(key)
account_address= acct.address

# Get tx receipt to get contract address
contract_address = Web3.toChecksumAddress("0x1064191A9b2981CC3Af7038E1c4F24B244bb8152") # deployed ata testnet gochain

# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

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

    #Control interface
    if action=='on':
         config=1
    if action=='off':
        config=0
    tx = contract_instance.functions.control(actuator,config).buildTransaction({'nonce': w3.eth.get_transaction_count(account_address),'gas': 3000000, 'gasPrice': Web3.toWei('2000', 'gwei')})
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=key)
    tx_hash= w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print('Transaction submitted:', tx_hash.hex())
    y=format(contract_instance.functions.pinStatus(actuator).call())
    print('Pin Status Changed: ', y)
    if y=="1":
        GPIO.output(actuator,GPIO.HIGH)
    else:
        GPIO.output(actuator,GPIO.LOW)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
