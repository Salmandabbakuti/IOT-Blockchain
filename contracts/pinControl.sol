pragma solidity ^0.5.0;

contract homeAutomation{
    
   address owner;
   constructor() public {
       owner=msg.sender;
          }

   struct pin{
      uint status;
   }
   
   mapping(uint=>pin) public pinStatus;
   
  function control(uint _pin, uint _status)public {
       require(msg.sender==owner);
       pinStatus[_pin].status=_status;
    }

}
    
