import json

class AccountsDto:

    def __init__ (self, idn: str):
        self.idn = idn
        print(self.get_account_public_key())

    def get_account_public_key(self):
        accounts_file = open(r'User/Databases/accounts.json')
        accounts_file_data = accounts_file.read()
        accounts_file_obj = json.loads(accounts_file_data)
        accounts_file.close()
        return accounts_file_obj['account_list'][self.idn]['public_key']  

    def get_account_private_key (self):
        accounts_file = open(r'User/Databases/accounts.json')
        accounts_file_data = accounts_file.read()
        accounts_file_obj = json.loads(accounts_file_data)
        accounts_file.close()
        return accounts_file_obj['account_list'][self.idn]['private_key']  