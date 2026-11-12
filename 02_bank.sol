
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleBank {

    mapping(address => uint) public balance;

    // Accept Ether during deployment
    constructor() payable {
        balance[msg.sender] = msg.value;
    }

    function deposit() public payable {
        require(msg.value > 0, "Send some Ether");
        balance[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0, "Invalid amount");
        require(balance[msg.sender] >= amount, "Insufficient balance");

        balance[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");
    }

    function showBalance() public view returns (uint) {
        return balance[msg.sender];
    }
}
