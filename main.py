from central.block import Block
from central.core import generatePrivateKey, generatePublicKey
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

key = RSA.generate(2048)

generatePrivateKey(key)
generatePublicKey(key)

currentInit = 500

