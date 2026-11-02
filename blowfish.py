from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(16)
iv = os.urandom(8)
msg = "Hello Blowfish!"

pad = padding.PKCS7(64).padder()
data = pad.update(msg.encode()) + pad.finalize()

cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
enc = cipher.encryptor()
encrypted = enc.update(data) + enc.finalize()

dec = cipher.decryptor()
decrypted = dec.update(encrypted) + dec.finalize()

unpad = padding.PKCS7(64).unpadder()
original = unpad.update(decrypted) + unpad.finalize()

print("Encrypted:", encrypted)
print("Decrypted:", original.decode())