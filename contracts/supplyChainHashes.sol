/// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract supplyChain {

    address public manager; // contract manager
    mapping (address => bool) public admins; // administrators who can manipulate (create and append) the hashes

    uint public numRecord = 0;
    mapping (uint => string[]) public hashes; // id -> hash[] list

    constructor () {
        manager = msg.sender; // set contract creator as manager
        admins[manager] = true; // contract manager is also the administrator
    }
    
    // only contract manager can add admin
    function addAdmin(address admin) public isManager {
        admins[admin] = true;
    }

    // create a new food supply chain (invoke when you don't know the food id)
    function createSupplyChain(string memory hashValue) public isAdmin returns(uint foodID) {
        hashes[numRecord].push(hashValue);
        foodID = numRecord;
        numRecord++;

        return foodID; // food id of the new supply chain
    }

    // append a new hash value to an existing supply chain (invoke when you already know the food id)
    function addHash(uint foodID, string memory hashValue) public isAdmin returns(bool) {
        if (hashes[foodID].length == 0) { // cannot add hash to a previously non-existent supply chain to prevent bugs
            return false;
        } else {
            hashes[foodID].push(hashValue);
            return true;
        }
    }

    // get the length of the specified supply chian (not block chain)
    function getChainLength(uint foodID) public view returns(uint) {
        return hashes[foodID].length;
    }

    // get a hash value based on food id and index of the supply chain
    function getHash(uint foodID, uint index) public view returns(string memory) {
        return hashes[foodID][index];
    }

    // get a list (array) of hashes based on food id
    function getHashes(uint foodID) public view returns(string[] memory) {
        return hashes[foodID];
    }

    // check if the message sender is the contract manager
    modifier isManager() {
        require(msg.sender == manager, "Can only be executed by the manager");
        _;
    }

    // check if the message sender is assigned as an admin
    modifier isAdmin() {
        require(admins[msg.sender], "Can only be executed by the administrator");
        _;
    }
}
