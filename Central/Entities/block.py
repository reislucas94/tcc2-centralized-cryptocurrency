class Block:
    def __init__ (self, initValue, initDestination, dataSet, nonce, blockHash):
        self.initValue = initValue
        self.initDestination = initDestination
        self.dataSet = dataSet
        self.nonce = nonce
        self.blockHash = blockHash
