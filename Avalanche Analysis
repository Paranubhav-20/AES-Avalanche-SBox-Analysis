import matplotlib.pyplot as plt
from sbox_static import encrypt_aes_static
from sbox_dynamic import generate_dynamic_sbox, encrypt_aes_dynamic
from utils import hamming_distance

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


if __name__ == "__main__":
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
    plt.savefig("plots/avalanche_plot.png")
    plt.show()
