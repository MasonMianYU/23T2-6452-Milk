/// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract supplyChain {

    address public manager; // contract manager
    bool public disabled = false; // state to indicate if the contract has been disabled
    mapping (address => bool) public admins; // administrators who can manipulate (create and append) the hashes
    mapping (uint => string[]) public hashes; // id -> hash[] list

    constructor () {
        manager = msg.sender; // set contract creator as manager
        admins[manager] = true; // contract manager is also the administrator
    }
    
    // only contract manager can add admin
    function addAdmin(address admin) public notDisabled isManager {
        admins[admin] = true;
    }

    // only contract manager can disable the smart contract
    function disableContract() public notDisabled isManager returns (bool) {
        disabled = true;
        return true;
    }

    // append a new hash value to a supply chain
    function addHash(uint foodID, string memory hashValue) public notDisabled isAdmin returns(bool) {
        hashes[foodID].push(hashValue);
        return true;
    }

    // get the length of the specified supply chian (not block chain)
    function getChainLength(uint foodID) public view notDisabled returns(uint) {
        return hashes[foodID].length;
    }

    // get a hash value based on food id and index of the supply chain
    function getHash(uint foodID, uint index) public view notDisabled returns(string memory) {
        return hashes[foodID][index];
    }

    // get a list (array) of hashes based on food id
    function getHashes(uint foodID) public view notDisabled returns(string[] memory) {
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
    
    // check if the contract is disabled
    modifier notDisabled() {
        require(disabled == false, "The smart contract has been disabled");
        _;
    }
}
