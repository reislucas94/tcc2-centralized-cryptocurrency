import json
from py_linq import Enumerable

import sys
sys.path.append("..")
from User.Entities.Account import AccountList as AccountList

def push(from_idn: str, to_idn: str, amount: float):
    if check_if_valid_account(from_idn) and check_if_valid_account(to_idn):
        print ('valid accounts')

def check_if_valid_account(idn:str):
    try:
        file_out = open(r'User/Databases/accounts.json')
        accounts_file = file_out.read()
        accounts_file_obj = json.loads(accounts_file)
    except:
        raise
    else:
        if Enumerable(accounts_file_obj['account_list']) \
            .any(lambda x: x['idn'] == idn):
            return True
        else: 
            raise Exception("Account '{}' does not exist.".format(idn))
    

def check_if_has_balance(idn: str, amount: float):
    return True