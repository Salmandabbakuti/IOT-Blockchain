import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from EmulatorGUI import GPIO
from flask import Flask, render_template, request
#from RPiSim import GPIO
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [14, 15, 18, 23, 24, 25, 8,7, 12, 16, 20, 21, 2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
w3 = Web3(HTTPProvider("https://testnet-rpc.gochain.io/"))
# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/homeAutomation.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
key="<private key with 0x prefix>"
acct = w3.eth.account.privateKeyToAccount(key)
account_address= acct.address
# web3.py instance



# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get tx receipt to get contract address
contract_address = Web3.toChecksumAddress("0xf30bd40783da0c35819b61d4b6a4e1aaa604e9af") # deployed ata testnet gochain

# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

#Contro Interface
for i in pinList:
    print(i, 'Status: {}' .format(contract_instance.functions.pinStatus(i).call()))

app = Flask(__name__)
@app.route("/")
def index():
    templateData = {
            'title' : 'GPIO output Status!'
            }
    return render_template('index.html', **templateData)
	
@app.route("/<pin>/<action>")
def control(pin, action):
    contract_instance = w3.eth.contract(abi=abi, address=contract_address)
    
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
         config=1
    if action=='off':
        config=0
    tx = contract_instance.functions.control(actuator,config).buildTransaction({'nonce': w3.eth.getTransactionCount(account_address),'gas': 1728712, 'gasPrice': w3.toWei('10', 'gwei')})
    signed_tx = w3.eth.account.signTransaction(tx, key)
    tx_hash= w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    w3.eth.waitForTransactionReceipt(tx_hash)
    print("Transaction its Way..")
    y=format(contract_instance.functions.pinStatus(actuator).call())
    print(y)
    if y=="1":
        GPIO.output(actuator,GPIO.HIGH)
    else:
        GPIO.output(actuator,GPIO.LOW)
    templateData = {
        'title': "GPIO Control"
        }
    return render_template('index.html', **templateData)
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
     
	
#Developed by Salman Dabbakuti
