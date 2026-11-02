import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_hash(data, original_hash):
    return generate_hash(data) == original_hash

data = "this is a secret mssg"

h = generate_hash(data)

print("Hash:", h)
print("verification (correct data):", verify_hash(data, h))
print("verification(tampered data):", verify_hash("this is a tampered message", h))