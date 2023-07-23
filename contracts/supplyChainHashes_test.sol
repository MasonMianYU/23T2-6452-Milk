// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.00 <0.9.0;

import "remix_tests.sol";

import "remix_accounts.sol";
import "../contracts/supplyChainHashes.sol";

/// Inherit 'supplyChainHashes' contract
contract supplyChainTest is supplyChain {

    // Variables used to emulate different accounts
    address acc0;
    address acc1;
    address acc2;

    /// arbitrary strings as hash values for test
    string hashValue1 = "abc123";
    string hashValue2 = "abcde123";
    string hashValue3 = "abcdefg123";
    string hashValue4 = "abcdefghi123";
    string[] hashArray1 = [hashValue1, hashValue2];
    string[] hashArray2 = [hashValue3, hashValue4];

    /// helper function, compare two string arrays
    function compareStringArrays(string[] memory arr1, string[] memory arr2) internal pure returns (bool) {
        if (arr1.length != arr2.length) {
            return false;
        }

        for (uint i = 0; i < arr1.length; i++) {
            if (keccak256(bytes(arr1[i])) != keccak256(bytes(arr2[i]))) {
                return false;
            }
        }

        return true;
    }

    function beforeAll() public {
        // Initiate account variables
        acc0 = TestsAccounts.getAccount(0);
        acc1 = TestsAccounts.getAccount(1);
        acc2 = TestsAccounts.getAccount(2);
    }

    /// check manager
    function managerTest() public {
        Assert.equal(manager, acc0, 'Manager should be acc0'); 
    }

    /// create supply chain test, create a new supply chain and insert hashValue1 into it
    function createSupplyChainTest() public {
        Assert.equal(createSupplyChain(hashValue1), 0, 'Food id should be 0'); 
    }

    /// add (append) hash value test, add hashValue2 into the first supply chain
    function addHashTest() public {
        Assert.ok(addHash(0, hashValue2), 'Should be true'); 
    }

    /// append a hash value with a previously non-existent food id, this should fail and returns false
    function addHashFailure() public {
        Assert.equal(addHash(1, hashValue3), false, 'This should be false');
    }

    /// get chain length test
    function getChainLengthTest() public {
        Assert.equal(getChainLength(0), 2, 'Chain length should be 2');
    }

    /// getHash test, get two hash values separately
    function getHashTest() public {
        Assert.equal(getHash(0, 0), hashValue1, 'Hash value should be hashValue1');
        Assert.equal(getHash(0, 1), hashValue2, 'Hash value should be hashValue2');
    }

    /// getHashes test, get all hash values in a supply chain
    function getHashesTest() public {
        Assert.ok(compareStringArrays(getHashes(0), hashArray1), 'Hash values should be hashValue1 and hashValue2'); 
    }
    
    /// add admin test
    function addAdminTest() public {
        addAdmin(acc1);
        Assert.ok(admins[acc1], 'Acc1 should be admin'); 
    }

    /// set admin as a non-manager, this should fail
    function addAdminFailure() public {
        try this.addAdmin(acc2) {
            Assert.equal(admins[acc2], true, 'Method execution did not fail');
        } catch Error(string memory reason) {
            // Compare failure reason, check if it is as expected
            Assert.equal(reason, 'Can only be executed by the manager', 'Failed with unexpected reason');
        } catch Panic(uint /* errorCode */) { // In case of a panic
            Assert.ok(false , 'Failed unexpected with error code');
        } catch (bytes memory /*lowLevelData*/) {
            Assert.ok(false, 'Failed unexpectedly');
        }
    }

    /// create, append and read a supply chain as an admin, rather than manager
    /// #sender: account-1
    function manipulateSupplyChainAsAnAdminTest() public {
        Assert.equal(createSupplyChain(hashValue3), 1, 'Food id should be 1');
        Assert.ok(addHash(1, hashValue4), 'Should be true');
        Assert.ok(compareStringArrays(getHashes(1), hashArray2), 'Hash values should be hashValue3 and hashValue4'); 
    }

    /// manipulate a supply chain as a stranger address (non-manager and non-administrator), this should fail
    function manipulateAsAStrangerFailure() public {
        // create failure test
        try this.createSupplyChain(hashValue3) returns (uint foodID) {
            Assert.equal(foodID, 2, 'Method execution did not fail');
        } catch Error(string memory reason) {
            // Compare failure reason, check if it is as expected
            Assert.equal(reason, 'Can only be executed by the administrator', 'Failed with unexpected reason');
        } catch Panic(uint /* errorCode */) { // In case of a panic
            Assert.ok(false , 'Failed unexpected with error code');
        } catch (bytes memory /*lowLevelData*/) {
            Assert.ok(false, 'Failed unexpectedly');
        }

        // add failure test
        try this.addHash(1, hashValue3) returns (bool state) {
            Assert.equal(state, true, 'Method execution did not fail');
        } catch Error(string memory reason) {
            // Compare failure reason, check if it is as expected
            Assert.equal(reason, 'Can only be executed by the administrator', 'Failed with unexpected reason');
        } catch Panic(uint /* errorCode */) { // In case of a panic
            Assert.ok(false , 'Failed unexpected with error code');
        } catch (bytes memory /*lowLevelData*/) {
            Assert.ok(false, 'Failed unexpectedly');
        }
    }
}
