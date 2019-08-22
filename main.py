from Central.Entities.Block import Block
from Central.CentralCore import *
from Central.CentralCore import *
from Crypto.PublicKey import RSA #https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

key = RSA.generate(2048)

#generatePrivateKey(key)
#generatePublicKey(key)

#currentInit = 500


#CentralRoutine
init_value = get_block_init()
init_destination = get_init_destination()
get_all_transfers()
put_into_block()
check_if_transfers_signatures_are_ok()
check_if_transfers_have_funds()

#MiningRoutine
calculate_hash_of_transfers_by_pairs()
calculate_block_hash()
signalize_everything_is_fine()

#CentralRoutine
publish_block()