//SPDX-License-Identifier:MIT

pragma solidity 0.8.20;

import '@chainlink/contracts/src/v0.6/interface/AggregatorV3Interface.sol';
contract fundme{

    mapping(address => uint256) public addresstoamountFunded;

    address[] public funders;

    constructor() publicowner{
        owner = msg.sender;
    }


    function fund() public payable {
        uint256 minimumUSD = 50 * 10 *18;
        require(getconvert(msg.value)>= minimumUSD);
        addresstoamountFunded[msg.sender] += msg.value;

        funders.push(msg.sender);

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

    modifier  onlyowner{
        require(msg.sender == owner);
        -;
    }

    
    function withdraw() payable public {
        require(msg.dender == owner);
        msg.sender.transfer(address(this).balance);
        for(uint256 funderIndex=0;funderIndex<funders.length;funderIndex++){
            address funder = funders[funderIndex];
            addresstoamountFunded[funder] = 0 ;
        }
        funders = new address[](0);
    }
}