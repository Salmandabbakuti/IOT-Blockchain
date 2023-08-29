// SPDX-License-Identifier: MIT
pragma solidity 0.8.21;

contract PinController {
    address owner;

    constructor() {
        owner = msg.sender;
    }

    enum PinStatus {
        Off,
        On
    }
    mapping(uint8 => PinStatus) public pinStatus;

    function setPinStatus(uint8 _pin, PinStatus _pinStatus) public {
        require(msg.sender == owner);
        pinStatus[_pin] = _pinStatus;
    }
}
