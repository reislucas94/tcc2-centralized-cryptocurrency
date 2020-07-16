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

# def _get_txdataset_hash(tx_dataset):
#     hashes = []
#     for i in range(len(tx_dataset)):
#         tx_hash = _get_tx_hash(list(tx_dataset)[i],tx_dataset[list(tx_dataset)[i]])
#         hashes.append(tx_hash)
#     hash_sum = ""
#     for j in range(len(hashes)):
#         hash_sum+=hashes[j]
#     return SHA256.new(bytearray(hash_sum, 'ascii')).hexdigest()

# def _get_tx_hash(tx_part:str, signature_part:str):
#     hash_tx_part = SHA256.new(bytearray(tx_part, 'ascii')).hexdigest()
#     hash_signature_part = SHA256.new(bytearray(signature_part, 'ascii')).hexdigest()
#     hashed_tx = SHA256.new(bytearray(hash_tx_part+hash_signature_part, 'ascii')).hexdigest()
#     return hashed_tx