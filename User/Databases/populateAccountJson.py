import json

file_out = open(r'User/Databases/accounts.json')
data = file_out.read()

dataObj = json.loads(data)



print (dataObj[0].get('IDN'))