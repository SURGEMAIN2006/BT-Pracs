from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(32)
iv = os.urandom(16)
msg = "Hello AES!"

pad = padding.PKCS7(128).padder()
data = pad.update(msg.encode()) + pad.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
enc = cipher.encryptor()
encrypted = enc.update(data) + enc.finalize()

dec = cipher.decryptor()
decrypted = dec.update(encrypted) + dec.finalize()

unpad = padding.PKCS7(128).unpadder()
original = unpad.update(decrypted) + unpad.finalize()

print("Encrypted AES:", encrypted)
print("Decrypted AES:", original.decode())