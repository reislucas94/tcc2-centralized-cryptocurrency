from py_linq import Enumerable

class Transaction:
    #A transaction is a comma-separated string.
    #First slot represents the date-time that the 'Add Transaction' button has been pushed
    #Second slot represents the sender idn
    #Third slot represents the value that was transfered
    #Fourth slot represents the receiver idn

    def __init__ (self, tx_string: str):
        self.tx_string = tx_string

    def get_transaction_timestamp(self):
        return self.tx_string.split(";")[0]

    def get_sender_idn (self):
        return self.tx_string.split(";")[1]
    
    def get_amount_transfered (self):
        return float(self.tx_string.split(";")[2])

    def get_receiver_idn (self):
        return self.tx_string.split(";")[3].split(":")[0]
