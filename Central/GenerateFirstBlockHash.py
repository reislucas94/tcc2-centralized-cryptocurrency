import json
from Crypto.Hash import SHA256

file_out = open(r'Central/Databases/Blocks/block0.json')
data = file_out.read()
file_out.close()

#Gets data from file and puts into data_obj
data_obj = json.loads(data)

hash_init_value = SHA256.new(bytearray(str(data_obj['init_value']), 'ascii')).hexdigest()
hash_init_destination = SHA256.new(bytearray(data_obj['init_destination'], 'ascii')).hexdigest()
hash_init = SHA256.new(bytearray(hash_init_value+hash_init_destination, 'ascii')).hexdigest()
hash_tx_dataset = 'none'
#hashDataSet = SHA256.new(bytearray(data_obj['dataSet'], 'ascii')).hexdigest()
hash_block_nonce = SHA256.new(bytearray(str(data_obj['block_nonce']), 'ascii')).hexdigest()

data_obj['block_hash'] = SHA256.new(bytearray(hash_init+hash_tx_dataset+hash_block_nonce, 'ascii')).hexdigest()

#While block_hash does not start with '000'...
while (data_obj['block_hash'][0] != '0') or (data_obj['block_hash'][1] != '0') or (data_obj['block_hash'][2] != '0'):
    data_obj['block_nonce']+=1
    hash_block_nonce = SHA256.new(bytearray(str(data_obj['block_nonce']), 'ascii')).hexdigest()
    data_obj['block_hash'] = SHA256.new(bytearray(hash_init+hash_tx_dataset+hash_block_nonce, 'ascii')).hexdigest()

#Convert data_obj to json
data = json.dumps(data_obj)

file_out = open("Central/Databases/Blocks/block1.json", "w")
#Writes JSON to file
file_out.write(data)

print(data_obj['block_hash'])

print(data_obj)