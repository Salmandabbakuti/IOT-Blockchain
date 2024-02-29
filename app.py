#  * SPDX-License-Identifier: MIT
#  * Licensed to @Author: Salman Dabbakuti(https://github.com/Salmandabbakuti)
#  * See the License for the specific language governing permissions and limitations under the License.

import json
from web3 import Web3, HTTPProvider
# import RPi.GPIO as GPIO # for real rasp-pi
from RPiSim.GPIO import GPIO
from flask import Flask, render_template

# Pin mapping
pin_mapping = {
    'fourteen': 14,
    'fifteen': 15,
    'eighteen': 18,
    'twentythree': 23,
    'twentyfour': 24,
    'twentyfive': 25,
    'eight': 8,
    'seven': 7,
    'twelve': 12,
    'sixteen': 16,
    'twenty': 20,
    'twentyone': 21,
    'two': 2,
    'three': 3,
    'four': 4,
    'seventeen': 17,
    'twentyseven': 27,
    'twentytwo': 22,
    'ten': 10,
    'nine': 9,
    'eleven': 11,
    'five': 5,
    'six': 6,
    'thirteen': 13,
    'nineteen': 19,
    'twentysix': 26
}

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = list(pin_mapping.values())
for pin in pinList:
    GPIO.setup(pin, GPIO.OUT)

# Load contract artifacts
artifacts_path = './artifacts/contracts/PinController.sol/PinController.json'
with open(artifacts_path) as artifacts_file:
    artifacts = json.load(artifacts_file)
abi = artifacts['abi']
bytecode = artifacts['bytecode']

# Initialize web3.py instance
w3 = Web3(HTTPProvider("http://localhost:8545/"))

# Deploy contract and get contract instance
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print('Contract deployed at:', tx_receipt.contractAddress)
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Get initial pin status
for i in pinList:
    pin_status = contract_instance.functions.pinStatus(i).call()
    print(f'Pin {i} status is {pin_status}')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<pin_id>/<action>")
def set_pin_status(pin_id, action):
    if pin_id not in pin_mapping:
        return render_template('index.html')

    pin_number = pin_mapping[pin_id]
    pin_status = 1 if action == 'on' else 0

    tx_hash = contract_instance.functions.setPinStatus(pin_number, pin_status).transact({'from': w3.eth.accounts[0]})
    print('Transaction submitted:', tx_hash.hex())

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print('Transaction confirmed in block:', tx_receipt.blockNumber)

    pin_status = contract_instance.functions.pinStatus(pin_number).call()
    print(f'Pin {pin_number} status changed to {pin_status}')

    GPIO.output(pin_number, GPIO.HIGH if pin_status else GPIO.LOW)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
