//SPDX-License-Identifier:MIT

pragma solidity 0.8.20;


contract fundme{

    mapping(address => uint256) public addresstoamountFunded;


    function fund() public payable {
        addresstoamountFunded[msg.sender] += msg.value;

        //ETH to Rupees conversion Rate
        //Decetralized oracle

    }
}