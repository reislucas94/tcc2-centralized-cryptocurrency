from Central.Entities.block import Block
from Central.CentralCore import *
from Central.CentralCore import *
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

#key = RSA.generate(2048)

#generatePrivateKey(key)
#generatePublicKey(key)

#currentInit = 500


#CentralRoutine
initValue = getBlockInit()
initDestination = getInitDestination()
getAllTransfers()
putIntoBlock()
checkIfTransfersSignaturesAreOk()
checkIfTransfersHaveFunds()

#MiningRoutine
calculateHashOfTransfersByPairs()
calculateBlockHash()
signalizeEverythingIsFine()

#CentralRoutine
publishBlock()