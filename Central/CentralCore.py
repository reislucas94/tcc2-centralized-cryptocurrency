import os
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

def generatePublicKey(key):
    private_key = key.export_key()
    file_out = open("central/keyring/privateK.pem", "wb")
    file_out.write(private_key)

def generatePrivateKey(key):
    public_key = key.publickey().export_key()
    file_out = open("central/keyring/publicK.pem", "wb")
    file_out.write(public_key)

def getBlockInit():
    return 500

def getInitDestination():
    return "17040189003"

def getAllTransfers(input):
    return input

def putIntoBlock(input):
    return input

def publishBlock(input):
    return input

def getLastBlockNumber():
    #Detects last block number
    lastBlockNumber = 0 
    for filename in os.listdir('Central/Databases/Blocks/'):
        if filename.endswith('.json'):
            blockNumber = filename.replace('block','').replace('.json','')
            if int(blockNumber) >= lastBlockNumber : lastBlockNumber = int(blockNumber)
    return lastBlockNumber
