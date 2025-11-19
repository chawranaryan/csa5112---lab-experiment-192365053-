from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    padding_len = 8 - (len(data) % 8)
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    return data[:-data[-1]]

# --- Encryption ---
def triple_des_encrypt_cbc(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded = pad(plaintext)
    encrypted = cipher.encrypt(padded)
    return encrypted

# --- Decryption ---
def triple_des_decrypt_cbc(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted)

# ------------------ MAIN -------------------

# 24-byte (192-bit) key for 3DES
key = DES3.adjust_key_parity(get_random_bytes(24))

# 8-byte IV for CBC mode
iv = get_random_bytes(8)

plaintext = b"THIS IS A TOP SECRET MESSAGE"

print("Key: ", base64.b64encode(key).decode())
print("IV:  ", base64.b64encode(iv).decode())

ciphertext = triple_des_encrypt_cbc(plaintext, key, iv)
print("\nEncrypted (Base64):", base64.b64encode(ciphertext).decode())

decrypted = triple_des_decrypt_cbc(ciphertext, key, iv)
print("\nDecrypted:", decrypted.decode())