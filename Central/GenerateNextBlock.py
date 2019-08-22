import json, os
from CentralCore import get_last_block_number
from Crypto.Hash import SHA256

#Detects which block was the last generated one
last_block_number = get_last_block_number()

last_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number)
next_block_directory = 'Central/Databases/Blocks/block{}.json'.format(last_block_number+1)

file_out = open(last_block_directory, 'r')
last_block_data = file_out.read()
file_out.close()

#Gets data from file and puts into lastBlockDataObj
last_block_data_object = json.loads(last_block_data)


#----------------------------------------------------







# hashInitValue = SHA256.new(bytearray(str(dataObj['initValue']), 'ascii')).hexdigest()
# hashInitDestination = SHA256.new(bytearray(dataObj['initDestination'], 'ascii')).hexdigest()
# hashInit = SHA256.new(bytearray(hashInitValue+hashInitDestination, 'ascii')).hexdigest()
# hashDataSet = 'none'
# #hashDataSet = SHA256.new(bytearray(dataObj['dataSet'], 'ascii')).hexdigest()
# hashNonce = SHA256.new(bytearray(str(dataObj['nonce']), 'ascii')).hexdigest()

# dataObj['blockHash'] = SHA256.new(bytearray(hashInit+hashDataSet+hashNonce, 'ascii')).hexdigest()

# #While blockHash does not start with '000'...
# while (dataObj['blockHash'][0] != '0') or (dataObj['blockHash'][1] != '0') or (dataObj['blockHash'][2] != '0'):
#     dataObj['nonce']+=1
#     hashNonce = SHA256.new(bytearray(str(dataObj['nonce']), 'ascii')).hexdigest()
#     dataObj['blockHash'] = SHA256.new(bytearray(hashInit+hashDataSet+hashNonce, 'ascii')).hexdigest()

# #Convert dataObj to json
# data = json.dumps(dataObj)

# file_out = open("Central/Databases/Blocks/block1.json", "w")
# #Writes JSON to file
# file_out.write(data)

# print(dataObj['blockHash'])

# print(dataObj)