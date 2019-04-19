from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

def generatePublicKey(key):
    private_key = key.export_key()
    file_out = open("central/keyring/privateK.pem", "wb")
    file_out.write(private_key)

def generatePrivateKey(key):
    public_key = key.publickey().export_key()
    file_out = open("central/keyring/publicK.pem", "wb")
    file_out.write(public_key)