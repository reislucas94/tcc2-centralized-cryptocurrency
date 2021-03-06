import json, os
from .CentralCore import get_last_block_number
from Crypto.Hash import SHA256
from .Entities.Block import Block as Block
from .Entities.Transaction import Transaction as Transaction

#Detects which block was the last generated one
last_block_number = get_last_block_number()

last_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number)
next_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number+1)

file_out = open(last_block_directory, 'r')
last_block_data = file_out.read()
file_out.close()

#Gets data from file and puts into lastBlockDataObj
last_block_data_object = json.loads(last_block_data)
last_block_data_object = Block(last_block_data_object['previous_block_hash'],last_block_data_object['init_value'],last_block_data_object['init_destination'],last_block_data_object['tx_dataset'],last_block_data_object['block_nonce'],last_block_data_object['block_hash'],)

#----------------------------------------------------

new_block_previous_hash = last_block_data_object.block_hash
new_block_init_value = get_init_value()
new_block_init_destination = get_init_destination()
new_block_tx_dataset = get_tx_dataset()
new_block_nonce = 0

new_block_data_object = Block(new_block_previous_hash, new_block_init_value, new_block_init_destination, new_block_tx_dataset, new_block_nonce)


def get_init_value():
    return 500

def get_init_destination():
    return '67010953058'

def get_tx_dataset():
    return [Transaction("39620880080","17040189003", 500.3, ""),Transaction("17040189003","39620880080", 500.3, "")]