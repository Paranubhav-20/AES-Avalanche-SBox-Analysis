from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_aes_static(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext, AES.block_size)
    return cipher.encrypt(padded)
