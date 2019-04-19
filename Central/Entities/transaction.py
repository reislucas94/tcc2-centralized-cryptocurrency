class Transaction:
    def __init__ (self, senderIDN, receiverIDN, valueTransfered, senderSignature):
        self.senderIDN = senderIDN
        self.receiverIDN = receiverIDN
        self.valueTransfered = valueTransfered
        self.senderSignature = senderSignature
