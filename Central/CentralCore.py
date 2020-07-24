import os
import json
import time
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key
from .Entities.Transaction import Transaction as Transaction
from .Dto.AccountsDto import AccountsDto as AccountsDto
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Central.Merkle import Merkle as Merkle
from Central.Entities.Block import Block as Block

def generate_private_key(key):
    private_key = key.export_key()
    file_out = open("central/keyring/privateK.pem", "wb")
    file_out.write(private_key)

def generate_public_key(key):
    public_key = key.publickey().export_key()
    file_out = open("central/keyring/publicK.pem", "wb")
    file_out.write(public_key)

def form_transaction(time: float, sender_idn: str, amount_transfered: float, receiver_idn: str): 
    return str(time) + ';' + sender_idn + ';' + str(amount_transfered) + ';' + receiver_idn

def sign_transaction(tx : str):
    sender_idn = Transaction(tx).get_sender_idn()
    private_key = RSA.import_key(AccountsDto(sender_idn).get_account_private_key())
    hash_message = SHA256.new(tx.encode('utf-8'))
    signature = pkcs1_15.new(private_key).sign(hash_message)
    return signature

def check_signature(tx: str, signature):
    sender_idn = Transaction(tx).get_sender_idn()
    public_key = RSA.import_key(AccountsDto(sender_idn).get_account_public_key())
    hash_message = SHA256.new(tx.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(hash_message, signature)
    except (ValueError, TypeError):
        raise
    return True

def check_blockchain_consistency():
    last_block_number = get_last_block_number()
    for i in range(last_block_number+1):
        if i != 0:
            try:
                with open('Central/Databases/Blocks/block{}.json'.format(i)) as block_file:
                    block_json = json.load(block_file)
                    block_object = Block(block_json['timestamp'],
                                    block_json['previous_block_hash'],
                                    block_json['init_value'],
                                    block_json['init_destination'],
                                    block_json['tx_dataset'],
                                    block_json['block_nonce'],
                                    block_json['block_hash'])
                    hash_result = find_block_hash(block_object.timestamp, 
                                    block_object.previous_block_hash,
                                    block_object.init_value,
                                    block_object.init_destination,
                                    block_object.tx_dataset,
                                    block_object.block_nonce)
                    if hash_result == block_object.block_hash:
                        print('Block{} is valid.'.format(i))
                    else:
                        raise Exception("The hash of 'block{}' is wrong. The block might have been changed and is invalid.".format(i))
            except:
                raise
    

def find_block_hash(timestamp: float, previous_block_hash: str, init_value:float, init_destination:str, tx_dataset, block_nonce:int):
    init_time = time.time()

    hash_timestamp = SHA256.new(bytearray(str(timestamp), 'ascii')).hexdigest()

    hash_init_value = SHA256.new(bytearray(str(init_value), 'ascii')).hexdigest()
    hash_init_destination = SHA256.new(bytearray(init_destination, 'ascii')).hexdigest()
    hash_init = SHA256.new(bytearray(hash_init_value+hash_init_destination, 'ascii')).hexdigest()

    hash_tx_dataset = _get_txdataset_hash(tx_dataset)

    hash_block_nonce = SHA256.new(bytearray(str(block_nonce), 'ascii')).hexdigest()

    block_hash = SHA256.new(bytearray(hash_init+hash_tx_dataset+hash_block_nonce, 'ascii')).hexdigest()
    
    return block_hash

def _get_txdataset_hash(tx_dataset):
    transactions = []

    if isinstance(tx_dataset, dict):
        transactions = stringify_transactions(tx_dataset)
    else:
        transactions = tx_dataset

    merkle_tree = Merkle()
    merkle_tree.listoftransaction = transactions
    merkle_tree.create_tree()

    return merkle_tree.Get_Root_leaf()

def get_block_init():
    return 500

def get_init_destination():
    return "17040189003"

def get_all_transfers(input):
    return input

def put_into_block(input):
    return input

def publish_block(input):
    return input

def get_last_block_number():
    #Detects last block number
    last_block_number = 0 
    for filename in os.listdir('Central/Databases/Blocks/'):
        if filename.endswith('.json'):
            block_number = filename.replace('block','').replace('.json','')
            if int(block_number) >= last_block_number : last_block_number = int(block_number)
    return last_block_number

#Transforms transactions dictionary to array of strings
def stringify_transactions(tx_dataset):
    transactions = []
    for i in range(len(tx_dataset)):
        tx_str = list(tx_dataset)[i] + ":" + tx_dataset[list(tx_dataset)[i]]
        transactions.append(tx_str)
    return transactions

def check_all_balances():
    try:
        balances_dict = dict()
        with open('./User/Databases/accounts.json') as accounts_file:
            accounts_json = json.load(accounts_file)
            for idx, account in enumerate(accounts_json['account_list']):
                balances_dict[account['idn']] = _check_account_balance(account['idn'])
        balances_json = json.dumps(balances_dict, indent=4, sort_keys=True)
        # with open("balances_file.json", "w") as balances_file:
        #     balances_file.write(balances_json)
        #     balances_file.close()
    except:
        raise

def _check_account_balance(idn: str):
    last_block_number = get_last_block_number()
    current_balance=0
    for i in range(last_block_number+1):
        block_file = open('Central/Databases/Blocks/block{}.json'.format(i), 'r')
        block_file_data = block_file.read()
        block_file.close()
        block_data_object = json.loads(block_file_data)
        if block_data_object['init_destination'] == idn: 
            current_balance+=block_data_object['init_value']
        for tx in block_data_object['tx_dataset']:
            if Transaction(tx).get_sender_idn() == idn:
                current_balance-=Transaction(tx).get_amount_transfered()
            if Transaction(tx).get_receiver_idn() == idn:
                current_balance+=Transaction(tx).get_amount_transfered()
    print (current_balance)
    return current_balance