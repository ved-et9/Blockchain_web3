//SPDX-License-Identifier:MIT

pragma solidity 0.8.20;

import '@chainlink/contracts/src/v0.6/interface/AggregatorV3Interface.sol';
contract fundme{

    mapping(address => uint256) public addresstoamountFunded;


    function fund() public payable {
        addresstoamountFunded[msg.sender] += msg.value;

        //ETH to Rupees conversion Rate
        //Decetralized oracle

    }

    function getversion() public view returns(uint256){
        AggregatorV3Interface price=AggregatorV3Interface();
        return price.version();
    }

    function getprice() public view returns(uint256){
        AggregatorV3Interface price = AggregatorV3Interface();
        (,unit256,,,)=price.latestRoundData();
        return uint256(answer);

    }


    function getconvert(uint256 eth) public view returns(uint256){
        uint256 ethp=getprice();
        uint256 ethinusd=(ethp * eth)/1000000000000000;
        return ethinusd;

    }
}