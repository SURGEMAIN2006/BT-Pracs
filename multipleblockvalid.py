import hashlib
import json
import time

def hash_block(block):
    data = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(data).hexdigest()

def create_block(index, prev_hash, transactions):
    block = {
        "index": index,
        "timestamp": time.time(),
        "transactions": transactions,
        "previous_hash": prev_hash
    }
    block["hash"] = hash_block(block)
    return block

def validate(chain):
    for i in range(1, len(chain)):
        block = chain[i]
        previous = chain[i-1]

        if block["index"] != previous["index"] + 1:
            return False

        if block["previous_hash"] != previous["hash"]:
            return False

        data = {k: v for k, v in block.items() if k != "hash"}

        if hash_block(data) != block["hash"]:
            return False

    return True

chain = [create_block(0, "0", [])]

for i in range(1, 3):
    tx = [f"User{i} pays User{i+1} {10*j}" for j in range(1, 4)]
    chain.append(create_block(i, chain[-1]["hash"], tx))

for b in chain:
    print(json.dumps(b, indent=4))

print("Is blockchain valid?", validate(chain))