# blockchain_verification.py

import hashlib

def hash_transaction(transaction):
    """Generates a hash for a given transaction."""
    return hashlib.sha256(transaction.encode()).hexdigest()

def verify_transaction(transaction, expected_hash):
    """Verifies if a transaction's hash matches the expected hash."""
    return hash_transaction(transaction) == expected_hash

def verify_block(block, previous_block_hash):
    """Verifies if a block's hash matches the expected hash from the previous block."""
    block_data = block + previous_block_hash
    return hashlib.sha256(block_data.encode()).hexdigest()

def verify_chain(blocks):
    """Verifies the entire blockchain integrity by checking each block's hash."""
    for i in range(1, len(blocks)):
        if not verify_block(blocks[i]['data'], blocks[i-1]['hash']):
            return False
    return True
