from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key
from Crypto.Hash import SHA256
from Central.Merkle import Merkle as Merkle
import time
from Central.CentralCore import stringify_transactions

def mine_block(timestamp: float, previous_block_hash: str, init_value:float, init_destination:str, tx_dataset, block_nonce:int):
    init_time = time.time()

    hash_timestamp = SHA256.new(bytearray(str(timestamp), 'ascii')).hexdigest()

    hash_init_value = SHA256.new(bytearray(str(init_value), 'ascii')).hexdigest()
    hash_init_destination = SHA256.new(bytearray(init_destination, 'ascii')).hexdigest()
    hash_init = SHA256.new(bytearray(hash_init_value+hash_init_destination, 'ascii')).hexdigest()

    hash_tx_dataset = _get_txdataset_hash(tx_dataset)

    hash_block_nonce = SHA256.new(bytearray(str(block_nonce), 'ascii')).hexdigest()

    block_hash = SHA256.new(bytearray(hash_init+hash_tx_dataset+hash_block_nonce, 'ascii')).hexdigest()

    #While block_hash does not start with '000'...
    while (block_hash[0] != '0') or (block_hash[1] != '0') or (block_hash[2] != '0'): #or (block_hash[3] != '0') or (block_hash[4] != '0'):
        block_nonce+=1
        hash_block_nonce = SHA256.new(bytearray(str(block_nonce), 'ascii')).hexdigest()
        block_hash = SHA256.new(bytearray(hash_init+hash_tx_dataset+hash_block_nonce, 'ascii')).hexdigest()

    final_time = time.time()

    total_time = final_time - init_time
    
    return [block_hash,block_nonce]

def _get_txdataset_hash(tx_dataset):
    transactions = []

    transactions = stringify_transactions(tx_dataset)

    merkle_tree = Merkle()
    merkle_tree.listoftransaction = transactions
    merkle_tree.create_tree()

    return merkle_tree.Get_Root_leaf()