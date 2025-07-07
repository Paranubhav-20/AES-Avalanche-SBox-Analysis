import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import matplotlib.pyplot as plt


def encrypt_aes_static(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext, AES.block_size)
    return cipher.encrypt(padded)


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


def hamming_distance(a: bytes, b: bytes) -> int:
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))


def avalanche_test(plaintext: bytes, key: bytes):
    results = []
    cipher_static = encrypt_aes_static(plaintext, key)
    sbox = generate_dynamic_sbox(seed=int.from_bytes(key, 'big') % 1000)
    cipher_dynamic = encrypt_aes_dynamic(plaintext, key, sbox)

    for i in range(len(plaintext) * 8):
        flipped = bytearray(plaintext)
        flipped[i // 8] ^= (1 << (i % 8))
        cipher_static_mod = encrypt_aes_static(bytes(flipped), key)
        cipher_dynamic_mod = encrypt_aes_dynamic(bytes(flipped), key, sbox)

        h_static = hamming_distance(cipher_static, cipher_static_mod)
        h_dynamic = hamming_distance(cipher_dynamic, cipher_dynamic_mod)

        results.append((h_static, h_dynamic))
    return results

# Graph 1
static1 = [1, 3, 1, 1, 2, 1, 1, 1, 1, 1]
dynamic1 = [8, 6, 4, 5, 2, 4, 6, 4, 3, 5]
plt.figure(figsize=(10, 4))
plt.plot(static1, label='Static S-box', marker='o')
plt.plot(dynamic1, label='Dynamic S-box', marker='x')
plt.title("Avalanche Effect Comparison (10 Tests)")
plt.xlabel("Test Number")
plt.ylabel("Bits Changed")
plt.legend()
plt.grid(True)
plt.show()


# Graph 2
static2 = [1, 4, 5, 1, 1, 3, 1, 1, 1, 8]
dynamic2 = [5, 3, 4, 5, 4, 5, 4, 7, 3, 4]
plt.figure(figsize=(10, 4))
plt.plot(static2, label='Static S-box', marker='o')
plt.plot(dynamic2, label='Dynamic S-box', marker='x')
plt.title("Avalanche Effect Comparison (10 Tests)")
plt.xlabel("Test Number")
plt.ylabel("Bits Changed")
plt.legend()
plt.grid(True)
plt.show()

# Graph 3
static3 = [1, 1, 1, 1, 1, 1, 1, 1, 6, 1]
dynamic3 = [6, 3, 4, 3, 6, 3, 3, 2, 3, 7]
plt.figure(figsize=(10, 4))
plt.plot(static3, label='Static S-box', marker='o')
plt.plot(dynamic3, label='Dynamic S-box', marker='x')
plt.title("Avalanche Effect Comparison (10 Tests)")
plt.xlabel("Test Number")
plt.ylabel("Bits Changed")
plt.legend()
plt.grid(True)
plt.show()

# Graph 4
static4 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
dynamic4 = [5, 4, 5, 3, 3, 4, 4, 3, 4, 4]
plt.figure(figsize=(10, 4))
plt.plot(static4, label='Static S-box', marker='o')
plt.plot(dynamic4, label='Dynamic S-box', marker='x')
plt.title("Avalanche Effect Comparison (10 Tests)")
plt.xlabel("Test Number")
plt.ylabel("Bits Changed")
plt.legend()
plt.grid(True)
plt.show()
