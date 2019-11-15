import json
from py_linq import Enumerable
from .CentralCore import get_last_block_number
from .CentralCore import stringify_transactions
from py_linq import Enumerable
from Central.Entities.Transaction import Transaction
import sys
sys.path.append("..")
from User.Entities.Account import AccountList as AccountList
from Central.Entities.Block import Block as Block
import time
from Central.MiningCore import mine_block

CURRENT_BLOCK_TRANSACTIONS = {}
CURRENT_BLOCK_INIT_DESTINATION = '39620880080'
CURRENT_BLOCK_INIT_VALUE = 0.0

def push_transaction(tx: str, sender_idn: str, receiver_idn: str, amount: float, sender_signature: str ):
    global CURRENT_BLOCK_TRANSACTIONS
    
    if __check_signature_authenticity(sender_idn, sender_signature) and \
        __check_if_has_balance(sender_idn, amount):
        
        CURRENT_BLOCK_TRANSACTIONS[tx] = sender_signature.hex()

def _check_if_valid_account(idn:str):
    try:
        file_out = open(r'User/Databases/accounts.json')
        accounts_file = file_out.read()
        accounts_file_obj = json.loads(accounts_file)
    except:
        raise
    else:
        if Enumerable(accounts_file_obj['account_list']) \
            .any(lambda x: x['idn'] == idn): 
            return True
        else: 
            raise Exception("Account '{}' does not exist.".format(idn))
    
def __check_signature_authenticity(sender_idn: str, sender_signature: str):
    return True

def __check_if_has_balance(sender_idn: str, amount_transfered: float):
    last_block_number = get_last_block_number()
    current_balance=0
    global CURRENT_BLOCK_INIT_DESTINATION
    global CURRENT_BLOCK_INIT_VALUE
    global CURRENT_BLOCK_TRANSACTIONS
    for i in range(last_block_number+1):
        block_file = open('Central/Databases/Blocks/block{}.json'.format(i), 'r')
        block_file_data = block_file.read()
        block_file.close()
        block_data_object = json.loads(block_file_data)
        if block_data_object['init_destination'] == sender_idn: 
            current_balance+=block_data_object['init_value']
        if CURRENT_BLOCK_INIT_DESTINATION == sender_idn:
            current_balance+=CURRENT_BLOCK_INIT_VALUE
        for tx in block_data_object['tx_dataset']:
            if Transaction(tx).get_sender_idn() == sender_idn:
                current_balance-=Transaction(tx).get_amount_transfered()
            if Transaction(tx).get_receiver_idn() == sender_idn:
                current_balance+=Transaction(tx).get_amount_transfered()
        for tx in CURRENT_BLOCK_TRANSACTIONS:
            if Transaction(tx).get_sender_idn() == sender_idn:
                current_balance-=Transaction(tx).get_amount_transfered()
            if Transaction(tx).get_receiver_idn() == sender_idn:
                current_balance+=Transaction(tx).get_amount_transfered()
            
    # check also in the block being added
    if current_balance>=amount_transfered:
        return True
    else: 
        raise Exception("Sender '{}' does not have balance for this transaction.".format(sender_idn))

def push_block():
    global CURRENT_BLOCK_INIT_DESTINATION
    global CURRENT_BLOCK_INIT_VALUE
    global CURRENT_BLOCK_TRANSACTIONS

    last_block_number = get_last_block_number()
    last_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number)
    next_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number+1)
    file_out = open(last_block_directory, 'r')
    last_block_data = file_out.read()
    file_out.close()

    last_block_data_object = json.loads(last_block_data)
    last_block_data_object = Block(last_block_data_object['timestamp'],
        last_block_data_object['previous_block_hash'],
        last_block_data_object['init_value'],
        last_block_data_object['init_destination'],
        last_block_data_object['tx_dataset'],
        last_block_data_object['block_nonce'],
        last_block_data_object['block_hash'],)
 #----------------------------------------------------
    try:
        new_block_timestamp = float(time.time())
        new_block_previous_hash = last_block_data_object.block_hash
        new_block_init_value = CURRENT_BLOCK_INIT_VALUE
        new_block_init_destination = CURRENT_BLOCK_INIT_DESTINATION
        new_block_tx_dataset = CURRENT_BLOCK_TRANSACTIONS
        new_block_nonce = 0

        try:
            new_block_hash_and_nonce = mine_block(new_block_timestamp, 
                new_block_previous_hash, 
                new_block_init_value, 
                new_block_init_destination, 
                new_block_tx_dataset, 
                new_block_nonce)
        except:
            raise
    except:
        raise

    new_block_hash = new_block_hash_and_nonce[0]  
    new_block_nonce = new_block_hash_and_nonce[1]

    new_block_data_object = Block(new_block_timestamp, 
    new_block_previous_hash, 
    new_block_init_value, 
    new_block_init_destination, 
    new_block_tx_dataset, 
    new_block_nonce,
    new_block_hash)

    # new_block_obj = []
    # new_block_obj["timestamp"] = new_block_data_object.timestamp
    # new_block_obj["previous_block_hash"] = new_block_data_object.previous_block_hash
    # new_block_obj["init_value"] = new_block_data_object.init_value
    # new_block_obj["init_destination"] = new_block_data_object.init_destination
    # new_block_obj["tx_dataset"] = new_block_data_object.tx_dataset
    # new_block_obj["block_nonce"] = new_block_data_object.block_nonce
    # new_block_obj["block_hash"] = new_block_data_object.block_hash
    
    new_block_json_data = json.dumps(
        {"timestamp":new_block_data_object.timestamp, 
        "previous_block_hash":new_block_data_object.previous_block_hash,
        "init_value":new_block_data_object.init_value,
        "init_destination":new_block_data_object.init_destination,
        "tx_dataset": stringify_transactions(new_block_data_object.tx_dataset),
        "block_nonce": new_block_data_object.block_nonce,
        "block_hash":new_block_data_object.block_hash
        }
        , indent=4)

    with open(next_block_directory, "w") as new_block_file:
        new_block_file.write(new_block_json_data)
        new_block_file.close()
 