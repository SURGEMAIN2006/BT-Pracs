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

        data = json.dumps(self.__dict__, sort_keys=True)
        self.hash = hashlib.sha256(data.encode()).hexdigest()

    def display(self):
        print("Block Index:", self.index)
        print("Timestamp:", self.timestamp)
        print("Transactions:")
        for t in self.transactions:
            print("-", t)
        print("Previous Hash:", self.previous_hash)
        print("Hash:", self.hash)

transactions = [
    "Alice pays Bob 5 BTC",
    "Bob pays Charlie 2 BTC",
    "Charlie pays Dave 1 BTC"
]

b = Block(transactions)
b.display()