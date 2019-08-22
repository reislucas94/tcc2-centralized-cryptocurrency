from Crypto.PublicKey import RSA

def generate_public_key(key):
    private_key = key.export_key()
    return private_key

def generate_private_key(key):
    public_key = key.publickey().export_key()
    return public_key