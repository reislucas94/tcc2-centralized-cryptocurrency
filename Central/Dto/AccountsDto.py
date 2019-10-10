import json
from py_linq import Enumerable

class AccountsDto:

    def __init__ (self, idn: str):
        self.idn = idn
        print(self.get_account_public_key())

    def get_account_public_key(self):
        accounts_file = open(r'User/Databases/accounts.json')
        accounts_file_data = accounts_file.read()
        accounts_file_obj = json.loads(accounts_file_data)
        accounts_file.close()
        account_found = Enumerable(accounts_file_obj['account_list']).where(lambda x: x['idn']==self.idn).first()
        return account_found['public_key']

    def get_account_private_key (self):
        accounts_file = open(r'User/Databases/accounts.json')
        accounts_file_data = accounts_file.read()
        accounts_file_obj = json.loads(accounts_file_data)
        accounts_file.close()
        account_found = Enumerable(accounts_file_obj['account_list']).where(lambda x: x['idn']==self.idn).first()
        return account_found['private_key']