//SPDX-License-Identifier:MIT

pragma solidity 0.8.20;

contract overflow{
    function overflow() public view returns(uint8){
        uint 8 big=255;
        return big;

    }
}
 //use safemathchainlink