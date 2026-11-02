import hashlib
from datetime import datetime

data = input("Enter the data for the block: ")
difficulty = int(input("Enter difficulty level: "))

nonce = 0
previous_hash = "0" * 64

while True:
    text = data + previous_hash + str(nonce)
    h = hashlib.sha256(text.encode()).hexdigest()

    if h.startswith("0" * difficulty):
        break

    nonce += 1

print("\nBlock added to the blockchain:")
print("Block ID: 0")
print("Timestamp:", datetime.now())
print("Data:", data)
print("Previous Hash:", previous_hash)
print("Nonce:", nonce)
print("Hash:", h)