import hashlib
import json
from datetime import datetime

sender = input("Enter Sender Address: ")
recipient = input("Enter Recipient Address: ")
amount = float(input("Enter Transaction Amount: "))

block = {
    "timestamp": str(datetime.now()),
    "sender": sender,
    "recipient": recipient,
    "amount": amount,
    "previous_hash": "0" * 64,
    "nonce": 0
}

data = json.dumps(block, sort_keys=True)
block["current_hash"] = hashlib.sha256(data.encode()).hexdigest()

print("\n=== Secure Transaction Block Created ===")
for k, v in block.items():
    print(k, ":", v)