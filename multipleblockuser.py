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

num_blocks = int(input("Enter number of blocks: "))
tx_count = int(input("Enter transactions per block: "))

chain = [create_block(0, [], "0")]

for i in range(1, num_blocks):
    print(f"\n--- Block {i} ---")
    transactions = []

    for j in range(tx_count):
        print(f"Transaction {j+1}")
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = float(input("Amount: "))

        transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

    block = create_block(i, transactions, chain[-1]["hash"])
    chain.append(block)

print("\n=== BLOCKCHAIN ===")

for b in chain:
    print(json.dumps(b, indent=4))