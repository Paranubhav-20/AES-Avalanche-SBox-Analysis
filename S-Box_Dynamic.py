import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def generate_dynamic_sbox(seed=0):
    np.random.seed(seed)
    sbox = list(range(256))
    np.random.shuffle(sbox)
    return sbox

def substitute_bytes(data, sbox):
    return bytes([sbox[b] for b in data])

def encrypt_aes_dynamic(plaintext: bytes, key: bytes, sbox) -> bytes:
    substituted = substitute_bytes(plaintext, sbox)
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(substituted, AES.block_size)
    return cipher.encrypt(padded)
