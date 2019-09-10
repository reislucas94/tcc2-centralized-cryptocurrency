import json

def push(from_idn: str, to_idn: str, amount: float):
    check_if_valid_account(from_idn)
    check_if_valid_account(to_idn)
    print(from_idn)
    print(to_idn)
    print(amount)

def check_if_valid_account(idn:str):
    file_out = open(r'User/Databases/accounts.json')
    data = file_out.read()
    data_obj = json.loads(data)


def check_if_has_balance(idn: str, amount: float):
    return 1