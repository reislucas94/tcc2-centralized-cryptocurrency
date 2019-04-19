class Block:
    def __init__ (self, initValue, initGoesTo, dataSet, nonce, blockHash):
        self.initValue = initValue
        self.initGoesTo = initGoesTo
        self.dataSet = dataSet
        self.nonce = nonce
        self.blockHash = blockHash
