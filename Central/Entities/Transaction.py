class Transaction:
    def __init__ (self, sender_idn, receiver_idn, value_transfered, sender_signature):
        self.sender_idn = sender_idn
        self.receiver_idn = receiver_idn
        self.value_transfered = value_transfered
        self.sender_signature = sender_signature
