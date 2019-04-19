class Transaction:
    def __init__ (self, senderCpf, receiverCpf, valueTransfered, senderSignature):
        self.senderCpf = senderCpf
        self.receiverCpf = receiverCpf
        self.valueTransfered = valueTransfered
        self.senderSignature = senderSignature
