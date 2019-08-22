from typing import List

class Account(object):
    def __init__ (self, idn:str, public_key:str, private_key:str):
        self.idn = idn
        self.public_key = public_key
        self.private_key = private_key

class AccountList(object):
    def __init__ (self, account_list: List[Account]):
        self.account_list = account_list