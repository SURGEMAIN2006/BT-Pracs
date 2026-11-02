import hashlib
import json
import time

DIFFICULTY = 4

def create_block(index, transactions, prev_hash):
    block = {
        "index": index,
        "timestamp": time.time(),
        "transactions": transactions,
        "previous_hash": prev_hash,
        "nonce": 0
    }

    while True:
        data = json.dumps(block, sort_keys=True)
        h = hashlib.sha256(data.encode()).hexdigest()

        if h.startswith("0" * DIFFICULTY):
            block["hash"] = h
            return block

        block["nonce"] += 1

chain = []
prev_hash = "0"

for i in range(3):
    tx = [
        {"sender": f"User{i}", "recipient": f"User{i+1}",
         "amount": i * 10 + j}
        for j in range(3)
    ]

    block = create_block(i, tx, prev_hash)
    chain.append(block)
    prev_hash = block["hash"]

for b in chain:
    print(json.dumps(b, indent=4))