## IoT-and-Blockchain

#### Pre-Requisites

##### Npm packages

1. Truffle

```
npm install -g truffle
```

2. Pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
```

3. ganache-cli

```
npm install -g ganache-cli
```

4. web3.py

```
pip install web3
```

##### Pip packages
5. Flask

6. GPIO Emulator

```
pip install requirements.txt
```

##### Desktop App

7. Python
https://www.python.org/downloads/

#### STEPS
*** Make Sure prerequisites are installed***

1. Clone the repository into desktop

```
git clone https://github.com/Salmandabbakuti/IoT-and-Blockchain.git
```

2. Install required PiP dependencies

```pip install requirements.txt```

3. Instantiate Ganache-cli Private Network.

```
ganache-cli
```
4. Complie Smart contract

```
truffle compile //or truffle.cmd compile for windows
```
5. Run app

```
python app.py
```

##### Running from Remote network(gochain):

** make sure you modifed ```appRemote.py``` with account private key and have some go tokens in it **

```
python appRemote.py
```


Wait a moment. this will take a minute or two. after deployment of contract in private network, you will see status of each pin in your command line and Emulator on Screen.

6. Head into browser and type ```<Your computer ip>/``` and control through UI.

<img align=center src="https://github.com/Salmandabbakuti/IoT-and-Blockchain/blob/master/Screenshot%20(81).png">

Basically, it will write particular pin status on blockchain and retrieve it from the chain. and then activate pin confiuaration accordingly.

boom.

 © Salman Dabbakuti
