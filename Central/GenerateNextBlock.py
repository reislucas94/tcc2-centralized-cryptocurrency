import json, os
from CentralCore import getLastBlockNumber
from Crypto.Hash import SHA256

#Detects which block was the last generated one
lastBlockNumber = getLastBlockNumber()

lastBlockDirectory = 'Central/Databases/Blocks/block{}.json'.format(lastBlockNumber)
nextBlockDirectory = 'Central/Databases/Blocks/block{}.json'.format(lastBlockNumber+1)

file_out = open(lastBlockDirectory, 'r')
lastBlockData = file_out.read()
file_out.close()

#Gets data from file and puts into lastBlockDataObj
lastBlockDataObj = json.loads(lastBlockData)


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