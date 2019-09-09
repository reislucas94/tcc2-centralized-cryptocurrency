import json
from Crypto.PublicKey import RSA
from .UserCore import generate_private_key, generate_public_key
from .Entities.Account import Account as Account
from .Entities.Account import AccountList as AccountList


file_out = open(r'User/Databases/accounts.json')
data = file_out.read()

data_obj = json.loads(data)

for idx, account in enumerate(data_obj):
    account = Account(account['idn'], account['public_key'], account['private_key'])
    key = RSA.generate(1024)
    account.private_key = key.export_key().decode()
    account.public_key = key.publickey().export_key().decode()
    data_obj[idx] = account

data_obj = AccountList(data_obj)

#Convert data_obj to json
data = json.dumps(data_obj.__dict__, default=lambda o: o.__dict__)

file_out = open("User/Databases/accounts.json", "w")
#Writes JSON to file
file_out.write(data)

