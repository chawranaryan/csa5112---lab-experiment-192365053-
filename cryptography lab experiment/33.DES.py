# -----------------------------------------------------
#   SIMPLE DES EDUCATIONAL IMPLEMENTATION IN PYTHON
#   - 64-bit block
#   - 56-bit key
#   - 16 Feistel rounds
#   - XOR-based round function
#   - No external library
# -----------------------------------------------------

# 32-bit Feistel function
def feistel(right, subkey):
    return right ^ subkey     # simple XOR for teaching


# Rotate 56-bit key left by 1 bit
def rotate_left_56(key):
    msb = (key >> 55) & 1
    key = ((key << 1) & 0xFFFFFFFFFFFFFF) | msb
    return key


# Generate 16 round keys (each 32-bit)
def generate_subkeys(key):
    subkeys = []
    for _ in range(16):
        key = rotate_left_56(key)
        subkeys.append(key & 0xFFFFFFFF)  # use lower 32 bits
    return subkeys


# DES encryption block (64-bit)
def des_encrypt_block(block, key):
    # split into left & right 32-bit halves
    L = (block >> 32) & 0xFFFFFFFF
    R = block & 0xFFFFFFFF

    subkeys = generate_subkeys(key)

    for i in range(16):
        temp = R
        R = L ^ feistel(R, subkeys[i])
        L = temp

    # swap final halves (DES rule)
    cipher = (R << 32) | L
    return cipher


# DES decryption block (64-bit)
def des_decrypt_block(block, key):
    L = (block >> 32) & 0xFFFFFFFF
    R = block & 0xFFFFFFFF

    subkeys = generate_subkeys(key)

    for i in range(16):
        temp = R
        R = L ^ feistel(R, subkeys[15 - i])
        L = temp

    plain = (R << 32) | L
    return plain


# ------------------------------------------
# TEST PROGRAM
# ------------------------------------------
plaintext = 0x1234567890ABCDEF      # 64-bit data
key       = 0x133457799BBCDFF1      # 56-bit DES key

cipher = des_encrypt_block(plaintext, key)
decrypted = des_decrypt_block(cipher, key)

print("Plaintext : ", hex(plaintext))
print("Key       : ", hex(key))
print("Cipher    : ", hex(cipher))
print("Decrypted : ", hex(decrypted))
