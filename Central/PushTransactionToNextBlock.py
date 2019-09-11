import json
from py_linq import Enumerable
from .CentralCore import get_last_block_number
from py_linq import Enumerable
from Central.Entities.Transaction import Transaction
import sys
sys.path.append("..")
from User.Entities.Account import AccountList as AccountList

def push(from_idn: str, to_idn: str, amount: float):
    if __check_if_valid_account(from_idn) and \
        __check_if_valid_account(to_idn) and \
        __check_if_has_balance(from_idn, amount):
        
        print ('Transfer is valid')

def __check_if_valid_account(idn:str):
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
    

def __check_if_has_balance(sender_idn: str, amount_transfered: float):
    last_block_number = get_last_block_number()
    current_balance=0
    for i in range(last_block_number+1):
        block_file = open('Central/Databases/Blocks/block{}.json'.format(i), 'r')
        block_file_data = block_file.read()
        block_file.close()
        block_data_object = json.loads(block_file_data)
        if block_data_object['init_destination'] == sender_idn: 
            current_balance+=block_data_object['init_value']
        for tx in block_data_object['tx_dataset']:
            if Transaction(tx).get_sender_idn() == sender_idn:
                current_balance-=Transaction(tx).get_value_transfered()
            if Transaction(tx).get_receiver_idn() == sender_idn:
                current_balance+=Transaction(tx).get_value_transfered()
    # check also in the block being added
    if current_balance>=amount_transfered:
        return True
    else: 
        raise Exception("Sender '{}' does not have balance for this transaction.".format(sender_idn))