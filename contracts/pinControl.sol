pragma solidity ^0.5.0;

contract homeAutomation {
  address owner;

  constructor() public {
    owner = msg.sender;
  }

  struct pin {
    uint256 status;
  }

  mapping(uint256 => pin) public pinStatus;

  function control(uint256 _pin, uint256 _status) public {
    require(msg.sender == owner);
    pinStatus[_pin].status = _status;
  }
}
