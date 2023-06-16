// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;


contract simple{
    uint256   num;



    struct People{
        uint256 mynum;
        string name;
    }

    People public person = People({ mynum:6 ,name:"Vedant"});


    function store(uint256 fav_num) public {
        num=fav_num;

    }

    function retrive() public view returns (uint256){
        return  num; 
    }

}