// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;


contract simple{
    uint256   num;
    bool mybool;



    struct People{
        uint256 mynum;
        string name;
    }

    //static array People[3] public people;
    //dynamic array
    People[] public people;

    //People public person = People({ mynum:6 ,name:"Vedant"});

    mapping (string => uint256) public nametonumber;
    function store(uint256 fav_num) public {
        num=fav_num;

    }

    //function retrive() public view returns (uint256){
    //    return  num; 
    // }


    function add_person(string memory _name,uint256 number) public {
        people.push(People(number,_name));

        //maping
        nametonumber[_name]=number;

    }

}