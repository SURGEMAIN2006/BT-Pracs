import hashlib
import time
import json

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block.encode()).hexdigest()

b = Block(0, "Genesis Block", "0")

print("Block Index:", b.index)
print("Block Timestamp:", b.timestamp)
print("Block Data:", b.data)
print("Previous Hash:", b.previous_hash)
print("Current Hash:", b.hash)