from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


key = RSA.generate(1024)
private_key = key.export_key().decode()
public_key = key.publickey().export_key().decode()

message = 'This is the message.'

other_message = 'This is another message.'

got_private_key = RSA.import_key(private_key)
hash_message = SHA256.new(message.encode('utf-8'))
signature = pkcs1_15.new(got_private_key).sign(hash_message)

other_hash_message = SHA256.new(other_message.encode('utf-8'))
other_signature = pkcs1_15.new(key).sign(other_hash_message)

got_public_key = RSA.import_key(public_key)
print (pkcs1_15.new(got_public_key).verify(other_hash_message, signature))


