from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = "Hello DSA!"

signature = private_key.sign(message.encode(), hashes.SHA256())

try:
    public_key.verify(signature, message.encode(), hashes.SHA256())
    print("Signature valid? True")
except:
    print("Signature valid? False")