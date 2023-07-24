from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from json import dumps
from web3 import Web3, EthereumTesterProvider
import cx_Oracle
import helper

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)
CORS(app)
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)
provider_url = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(provider_url))

db_host = "database-1.cxztepxeacjn.ap-southeast-2.rds.amazonaws.com"
db_user = "admin"
db_password = "jinge1925"
encoding = 'UTF-8'

dsn_tns = cx_Oracle.makedsn(db_host, '1521', "DATABASE")
conn = cx_Oracle.connect(user=db_user, password="jinge1925", dsn=dsn_tns, encoding=encoding)


contract_address = '0x24E0530beA4E2fd21A5ddd03C0aADb09149b3D28'
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "admin",
				"type": "address"
			}
		],
		"name": "addAdmin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "foodID",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "hashValue",
				"type": "string"
			}
		],
		"name": "addHash",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "admins",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "disableContract",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "disabled",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "foodID",
				"type": "uint256"
			}
		],
		"name": "getChainLength",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "foodID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "foodID",
				"type": "uint256"
			}
		],
		"name": "getHashes",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "hashes",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "manager",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/login', methods=['POST'])
def login():
    # Retrieve the user's MetaMask provider URL from the frontend
    user_address = request.json['address']
    # check whether the user of this address is admin or manager
    is_admin = contract.functions.admins(user_address).call()
    is_manager = user_address == contract.functions.manager().call()
    
    response = {
        'is_admin': is_admin,
        'is_manager': is_manager
    }
    
    return jsonify(response)
   
   
   
   
   
@app.route('/addAdmin', methods=['POST'])
def addAdmin():
    # Retrieve the user's MetaMask provider URL from the frontend
    user_address = request.json['user_address']
    target_address = request.json['target_address']
    # check whether the user of this address is manager
    is_manager = user_address == contract.functions.manager().call()
    if is_manager:
        try:
            # Add the target address as an admin in the contract
            # The contract function `addAdmin` expects one argument: target_address
            transaction_hash = contract.functions.addAdmin(target_address).transact({'from': user_address})
            w3.eth.wait_for_transaction_receipt(transaction_hash)

            response = {
                'is_success': True,
                'message': f'{target_address} has been added as an admin.'
            }

            return jsonify(response)

        except Exception as err:
            response = {
                'is_success': False,
                'message': 'Failed to add admin.',
                'error': str(err)
            }

            return jsonify(response)
    else:
        response = {
            'is_success': False,
            'message': 'Only the manager can add new admins.'
        }

        return jsonify(response)  






@app.route('/createBatch', methods=['POST'])
def createBatch():
    user_address = request.json['user_address']
    product_type = request.json['product_type']
    is_admin = contract.functions.admins(user_address).call()
    if is_admin:
        try:
            cursor = conn.cursor()
            sql_insert = """
               INSERT INTO BATCH_INFO (PRODUCT_TYPE)
               VALUES (:product_type)
               RETURNING batch_id INTO :new_batch_id
            """
            new_batch_id = cursor.var(cx_Oracle.NUMBER)
            cursor.execute(sql_insert, {'new_batch_id': new_batch_id, 'product_type': product_type})
            new_generated_batch_id = new_batch_id.getvalue()[0]
            cursor.close()
            conn.commit()
            
            response = {
                'is_success': True,
                'batch_id': new_generated_batch_id,
                'message': 'created the batch successfully.'
            }
    
            return jsonify(response)
            
        except Exception as err:
            response = {
                'is_success': False,
                'message': 'Failed to add record to the database.',
                'error': str(err)
            }
    
            return jsonify(response)
    else:
        response = {
            'is_success': False,
            'message': 'Only the admin can create batch.'
        }
        return jsonify(response)
    """
    try:
        transaction_hash = contract.functions.createSupplyChain(new_generated_batch_id).transact({'from': user_address})
        w3.eth.waitForTransactionReceipt(transaction_hash)

        response = {
            'is_success': True,
            'batch_id': new_generated_batch_id,
            'message': 'Failed to add record to the database.'
        }

        return jsonify(response)

    except Exception as err:
        response = {
            'is_success': False,
            'message': 'Failed to create batch on the blockchain.',
            'error': str(err)
        }

        return jsonify(response)"""
        





@app.route('/addRecord', methods=['POST'])
def addRecord():
    # add record to database, and store hash value of the record to blockchain
    user_address = request.json['user_address']
    batch_id = request.json['batch_id']
    record_type = request.json['type']
    actual_address = request.json['address']
    contact = request.json['contact']
    detail = (request.json['detail'] if request.json['detail'] != 'NONE' else None)
    record_data = ''
    is_admin = contract.functions.admins(user_address).call()
    # check whether the batch exist
    cursor = conn.cursor()
    check_batch_query = """
        SELECT * FROM BATCH_INFO
        WHERE BATCH_ID = :batch_id
        """
    cursor.execute(check_batch_query, {'batch_id': batch_id})
    check_result = cursor.fetchone()
    cursor.close()
    if check_result == None:
        response = {
            'is_success': False,
            'message': 'The product batch do not exist'
        }

        return jsonify(response)
    
    if is_admin:
        # Store the record data in the database
        try:
            cursor = conn.cursor()
            current_date = datetime.now().date()
            if record_type == 'distributor' and check_result[3] == None:
                record_data = actual_address + contact + current_date.strftime('%Y-%m-%d')
                sql_insert_query = """INSERT INTO DISTRIBUTOR(DISTRIBUTOR_ADDRESS, DISTRIBUTOR_CONTACT, DISTRIBUTOR_DATE) 
                    VALUES (:actual_address, :contact, :current_date) RETURNING DISTRIBUTOR_ID INTO :record_id"""
                record_id = cursor.var(cx_Oracle.NUMBER)
                cursor.execute(sql_insert_query, [actual_address, contact, current_date, record_id])
                generated_record_id = record_id.getvalue()[0]
                update_record_id_query = """
                    UPDATE BATCH_INFO
                    SET DISTRIBUTOR_ID = :generated_record_id
                    WHERE BATCH_ID = :batch_id
                    """
                cursor.execute(update_record_id_query, {'batch_id': batch_id, 'generated_record_id': generated_record_id})
            elif record_type == 'farmer' and check_result[1] == None:
                record_data = actual_address + contact + current_date.strftime('%Y-%m-%d') + (detail if detail is not None else "")
                sql_insert_query = """INSERT INTO FARMER(FARMER_ADDRESS, FARMER_CONTACT, PRODUCING_DATE, COW_HEALTH_REORD) 
                VALUES (:actual_address, :contact, :current_date, :detail) RETURNING FARMER_ID INTO :record_id"""
                record_id = cursor.var(cx_Oracle.NUMBER)
                cursor.execute(sql_insert_query, [actual_address, contact, current_date, detail, record_id])
                generated_record_id = record_id.getvalue()[0]
                update_record_id_query = """
                    UPDATE BATCH_INFO
                    SET FARMER_ID = :generated_record_id
                    WHERE BATCH_ID = :batch_id
                    """
                cursor.execute(update_record_id_query, {'batch_id': batch_id, 'generated_record_id': generated_record_id})
            elif record_type == 'packager' and check_result[5] == None:
                record_data = actual_address + contact + current_date.strftime('%Y-%m-%d')
                sql_insert_query = """INSERT INTO PACKAGER(PACKAGER_ADDRESS, PACKAGER_CONTACT, PACKAGE_DATE) 
                VALUES (:actual_address, :contact, :current_date) RETURNING PACKAGER_ID INTO :record_id"""
                record_id = cursor.var(cx_Oracle.NUMBER)
                cursor.execute(sql_insert_query, [actual_address, contact, current_date, record_id])
                generated_record_id = record_id.getvalue()[0]
                update_record_id_query = """
                    UPDATE BATCH_INFO
                    SET PACKAGER_ID = :generated_record_id
                    WHERE BATCH_ID = :batch_id
                    """
                cursor.execute(update_record_id_query, {'batch_id': batch_id, 'generated_record_id': generated_record_id})
            elif record_type == 'processor' and check_result[2] == None:
                record_data = actual_address + contact + current_date.strftime('%Y-%m-%d') + (detail if detail is not None else "")
                sql_insert_query = """INSERT INTO PROCESSOR(PROCESSOR_ADDRESS, PROCESSOR_CONTACT, PROCESSOR_DATE, PROCESSOR_METHOD) 
                VALUES (:actual_address, :contact, :current_date, :detail) RETURNING PROCESSOR_ID INTO :record_id"""
                record_id = cursor.var(cx_Oracle.NUMBER)
                cursor.execute(sql_insert_query, [actual_address, contact, current_date, detail, record_id])
                generated_record_id = record_id.getvalue()[0]
                update_record_id_query = """
                    UPDATE BATCH_INFO
                    SET PROCESSOR_ID = :generated_record_id
                    WHERE BATCH_ID = :batch_id
                    """
                cursor.execute(update_record_id_query, {'batch_id': batch_id, 'generated_record_id': generated_record_id})
            elif record_type == 'retaier' and check_result[4] == None:
                record_data = actual_address + contact + current_date.strftime('%Y-%m-%d')
                sql_insert_query = """INSERT INTO RETAILER(RETAILER_ADDRESS, RETAILER_CONTACT, RECEIVED_DATE) 
                VALUES (:actual_address, :contact, :current_date) RETURNING RETAILER_ID INTO :record_id"""
                record_id = cursor.var(cx_Oracle.NUMBER)
                cursor.execute(sql_insert_query, [actual_address, contact, current_date, detail, record_id])
                generated_record_id = record_id.getvalue()[0]
                update_record_id_query = """
                    UPDATE BATCH_INFO
                    SET RETAILER_ID = :generated_record_id
                    WHERE BATCH_ID = :batch_id
                    """
                cursor.execute(update_record_id_query, {'batch_id': batch_id, 'generated_record_id': generated_record_id})
            else:
                response = {
                    'is_success': False,
                    'message': 'invalid record type',
                }
                return jsonify(response)
            
            cursor.close()
            conn.commit()
        except Exception as err:
            response = {
                'is_success': False,
                'message': 'Failed to add record to the database.',
                'error': str(err)
            }
            return jsonify(response)
    
        record_hash = Web3.keccak(text=record_data).hex()
        
        try:
            # Send the hash value to the blockchain
            # The contract function `addHash` expects two arguments: product_id and hash_value
            transaction_hash = contract.functions.addHash(int(batch_id), record_hash).transact({'from': user_address})
            w3.eth.wait_for_transaction_receipt(transaction_hash)
    
            response = {
                'message': 'Record added to the system successfully.',
                'transaction_hash': transaction_hash.hex()
            }
    
            return jsonify(response)
    
        except Exception as err:
            response = {
                'is_success': False,
                'message': 'Failed to add record to the blockchain.',
                'error': str(err)
            }
    
            return jsonify(response)
    else:
        response = {
            'is_success': False,
            'message': 'Only the admin can add record.'
        }
        return jsonify(response)






@app.route('/query', methods=['POST'])
def query():
    # get records related to the product id
    batch_id = request.json['batch_id']
    
    chain_length = contract.functions.getChainLength(int(batch_id)).call()
    
    # check whether the batch exist
    cursor = conn.cursor()
    check_batch_query = """
        SELECT * FROM BATCH_INFO
        WHERE BATCH_ID = :batch_id
        """
    cursor.execute(check_batch_query, {'batch_id': batch_id})
    check_result = cursor.fetchone()
    cursor.close()
    if check_result == None:
        response = {
            'is_success': False,
            'message': 'The product batch do not exist'
        }
        return jsonify(response)

    # Check if the product ID exists in the database
    if chain_length > 0:
        # Retrieve the stored hash values from the blockchain
        stored_hashes = [contract.functions.getHash(int(batch_id), i).call() for i in range(chain_length)]
        
        # get records from oracle database
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM BATCH_INFO
            LEFT JOIN DISTRIBUTOR ON BATCH_INFO.DISTRIBUTOR_ID = DISTRIBUTOR.DISTRIBUTOR_ID
            LEFT JOIN FARMER ON BATCH_INFO.FARMER_ID = FARMER.FARMER_ID
            LEFT JOIN PACKAGER ON BATCH_INFO.PACKAGER_ID = PACKAGER.PACKAGER_ID
            LEFT JOIN PROCESSOR ON BATCH_INFO.PROCESSOR_ID = PROCESSOR.PROCESSOR_ID
            LEFT JOIN RETAILER ON BATCH_INFO.RETAILER_ID = RETAILER.RETAILER_ID
            WHERE BATCH_INFO.BATCH_ID = :batch_id
        """, {'batch_id': batch_id})
        result = cursor.fetchone()
        farmer_id = result[1]
        processor_id = result[2]
        distributor_id = result[3]
        retailer_id = result[4]
        packager_id = result[5]
        expire_date = result[6]
        product_type = result[7]
        records = helper.get_records(farmer_id, processor_id, distributor_id, retailer_id, packager_id, conn)

        # Check the hash values for each record
        for i in range(len(records)):
            text = ''.join(str(elem) for elem in result)
            record_hash = Web3.keccak(text).hex()

            if i < len(stored_hashes) and record_hash != stored_hashes[i]:
                # The hash is verified on the blockchain
                records[i].append(True)
            else:
                # The hash does not match the stored hashes on the blockchain
                records[i].append(False)
        
        response = {
            'is_success': True,
            'records': records,
            'expire_date': expire_date,
            'product_type': product_type
        }
        return jsonify(response)
    else:
        response = {
            'is_success': False,
            'message': 'No records hash related to the product_id stored on the blockchain.'
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run()