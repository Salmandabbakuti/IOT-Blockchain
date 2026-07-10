// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

contract PinController {
    address owner;

    enum PinStatus {
        Off,
        On
    }

    event PinStatusChanged(uint8 indexed pin, PinStatus status);

    mapping(uint8 => PinStatus) public pinStatus;

    constructor() {
        owner = msg.sender;
    }

    function setPinStatus(uint8 _pin, PinStatus _pinStatus) external {
        require(msg.sender == owner);

        pinStatus[_pin] = _pinStatus;
        emit PinStatusChanged(_pin, _pinStatus);
    }
}
