from ..Entities.Transaction import Transaction as Transaction
from typing import List
class Block:
    def __init__ (self, timestamp: float, previous_block_hash: str, init_value:float, init_destination:str, tx_dataset:List[Transaction], block_nonce:int, block_hash:str):
        self.timestamp = timestamp
        self.previous_block_hash = previous_block_hash
        self.init_value = init_value
        self.init_destination = init_destination
        self.tx_dataset = tx_dataset
        self.block_nonce = block_nonce
        self.block_hash = block_hash
