import hashlib
import json
import time

def create_block(index, transactions, prev_hash):
    block = {
        "index": index,
        "timestamp": time.time(),
        "transactions": transactions,
        "previous_hash": prev_hash
    }

    data = json.dumps(block, sort_keys=True)
    block["hash"] = hashlib.sha256(data.encode()).hexdigest()
    return block

blockchain = []
prev_hash = "0"

for i in range(5):
    transactions = [
        {"sender": f"User{i}", "recipient": f"User{i+1}",
         "amount": i * 10 + j}
        for j in range(3)
    ]

    block = create_block(i, transactions, prev_hash)
    blockchain.append(block)
    prev_hash = block["hash"]

for block in blockchain:
    print(json.dumps(block, indent=4))