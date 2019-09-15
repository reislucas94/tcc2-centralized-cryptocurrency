import os
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key
from .Entities.Transaction import Transaction as Transaction
from .Dto.AccountsDto import AccountsDto as AccountsDto
from Crypto.Cipher import PKCS1_OAEP

def generate_private_key(key):
    private_key = key.export_key()
    file_out = open("central/keyring/privateK.pem", "wb")
    file_out.write(private_key)

def generate_public_key(key):
    public_key = key.publickey().export_key()
    file_out = open("central/keyring/publicK.pem", "wb")
    file_out.write(public_key)

def form_transaction(time: float, sender_idn: str, amount_transfered: float, receiver_idn: str): 
    return str(time) + ';' + sender_idn + ';' + str(amount_transfered) + ';' + receiver_idn

def sign_transaction(tx : str):
    sender_idn = Transaction(tx).get_sender_idn()
    private_key = RSA.import_key(AccountsDto(sender_idn).get_account_private_key())
    cipher = PKCS1_OAEP.new(key=private_key)
    cipher_text = cipher.encrypt(tx)
    return cipher_text

def check_signature(tx: str):
    return True

def get_block_init():
    return 500

def get_init_destination():
    return "17040189003"

def get_all_transfers(input):
    return input

def put_into_block(input):
    return input

def publish_block(input):
    return input

def get_last_block_number():
    #Detects last block number
    last_block_number = 0 
    for filename in os.listdir('Central/Databases/Blocks/'):
        if filename.endswith('.json'):
            block_number = filename.replace('block','').replace('.json','')
            if int(block_number) >= last_block_number : last_block_number = int(block_number)
    return last_block_number
