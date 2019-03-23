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
fourteen=14
fifteen=15
eighteen=18
twentythree=23
twentyfour=24
twentyfive=25
eight=8
seven=7
twelve=12
sixteen=16
twenty=20
twentyone=21
two=2
three=3
four=4
seventeen=17
twentyseven=27
twntytwo=22
ten=10
nine=9
eleven=11
five=5
six=6
thirteen=13
nineteen=19
twentysix=26

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

# compile your smart contract with truffle first
truffleFile = json.load(open('homeAutomation.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']

# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:8545/"))


# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)

# Getters + Setters for web3.eth.contract object
for i in pinList:
    print(i, 'Status: {}' .format(contract_instance.pinStatus(i)))
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

@app.route("/<pin>/<action>")
def control(pin, action):
     contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)
     contract_instance.control(pin,action,transact={'from': w3.eth.accounts[0]})
     print("Transaction its Way..")
     y=format(contract_instance.pinStatus(pin))
     if y=='1':
         GPIO.output(pin,GPIO.HIGH)
     else:
        GPIO.output(pin,GPIO.LOW)     
     
    
