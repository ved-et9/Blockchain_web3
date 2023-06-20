//SPDX-License_Identifier: MIT

// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "./simple.sol";

//inheritance
contract storage_factory is simple{

    
    simple[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        simple simpleStorage = new simple();
        simpleStorageArray.push(simpleStorage);
    }
    //interacting with deployed contracts

    function sfstored(uint256 _simpleStorageIndex,uint256 _simpleStorageNumber) public {
        //address
        //ABI (application binary Interface)
        //both needed to interact with contract
        simple simpleStorage = simple(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    function sfget(uint256 _simpleStorageIndex) public view returns (uint256){
        simple simpleStorage =simple(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrive();

    }
}