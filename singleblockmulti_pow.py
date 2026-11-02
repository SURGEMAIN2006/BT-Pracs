import hashlib
import json
import time

class Block:
    def __init__(self, transactions):
        self.index = 0
        self.timestamp = str(time.time())
        self.transactions = transactions
        self.previous_hash = "0" * 64
        self.nonce = 0

    def mine(self):
        while True:
            data = json.dumps(self.__dict__, sort_keys=True)
            h = hashlib.sha256(data.encode()).hexdigest()

            if h.startswith("00"):
                self.hash = h
                break

            self.nonce += 1

        print("Block mined:", self.hash)
        print("Nonce found:", self.nonce)

transactions = [
    "Alice pays Bob 5 BTC",
    "Bob pays Charlie 2 BTC",
    "Charlie pays Dave 1 BTC"
]

b = Block(transactions)
b.mine()

print("Block Index:", b.index)
print("Transactions:", b.transactions)
print("Previous Hash:", b.previous_hash)
print("Nonce:", b.nonce)
print("Hash:", b.hash)