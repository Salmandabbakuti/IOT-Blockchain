# IoT-and-Blockchain

A simple IoT and Blockchain based application to demonstrate the use of blockchain in IoT.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/en/download/)
- [Python](https://www.python.org/downloads/)
- Windows 8+ (for simulating GPIO pins on Windows), Raspberry Pi (for using actual GPIO pins)
- [Windows Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) - Only for Windows (Simulating GPIO pins on Windows)

> Note: _Windows Build Tools is required to install web3. Install through Powershell(Admin) if not installed already_

```bash
npm install -g windows-build-tools
```

### Steps

Before starting with app, you need to compile the smart contract and start a local blockchain. Follow the steps below to do so:

1. Install required dependencies:

```bash
npm install
```

2. Start a local blockchain using Hardhat:

```bash
npx hardhat node
```

3. Compile contract in a separate terminal:

```bash
npx hardhat compile
```

4. Install python dependencies and start the app:

```bash
pip install -r requirements.txt

python app.py
```

Open http://localhost:8000 in your browser to see the app and Interact with the IoT device.

### Demo

![screen](https://github.com/Salmandabbakuti/IoT-and-Blockchain/assets/29351207/4e684842-095e-4472-85fc-5621295ce6a3)

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used for the backend
- [Web3.py](https://web3py.readthedocs.io/en/stable/) - Python library for interacting with Ethereum blockchain
- [Hardhat](https://hardhat.org/) - Ethereum development environment for compiling, testing, deploying, and interacting with smart contracts
- [Solidity](https://docs.soliditylang.org/en/v0.8.4/) - Ethereum's smart contract programming language
- [GPIO Simulator](https://pypi.org/project/GPIOSimulator/) - Python library for simulating GPIO pins
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) - Python library for accessing GPIO pins on Raspberry Pi

## Safety

This is experimental software and subject to change over time.

This is a proof of concept and is not ready for production use. It is not audited and has not been tested for security. Use at your own risk. I do not give any warranties and will not be liable for any loss incurred through any use of this codebase.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
