/// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract supplyChain {

    address public manager; // Contract manager

    uint public numRecord = 0;
    mapping (uint => string[]) public hashes; // id -> hash[] list

    constructor () {
        manager = msg.sender; // Set contract creator as manager
    }
    
    // create a new food supply chain (invoke when you don't know the food id)
    function createSupplyChain(string memory hashValue) public restricted returns(uint foodID) {
        hashes[numRecord].push(hashValue);
        numRecord++;
        foodID = numRecord - 1;

        return foodID; // food id of the new supply chain
    }

    // append a new hash value to an existing supply chain (invoke when you already know the food id)
    function addHash(uint foodID, string memory hashValue) public restricted {
        hashes[foodID].push(hashValue);
    }

    function chainLength(uint foodID) public view returns(uint) {
        return hashes[foodID].length;
    }

    modifier restricted() {
        require(msg.sender == manager, "Can only be executed by the manager");
        _;
    }
}
