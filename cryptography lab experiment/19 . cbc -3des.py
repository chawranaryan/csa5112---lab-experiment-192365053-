# --- Simple 64-bit block XOR-based block cipher (fake 3DES for demo) ---

def simple_block_encrypt(block, key):
    return block ^ key  # XOR = simplified encryption

def simple_block_decrypt(block, key):
    return block ^ key  # symmetric

# --- CBC MODE IMPLEMENTATION ---

def encrypt_cbc(plaintext_blocks, key, iv):
    ciphertext = []
    prev = iv
    for block in plaintext_blocks:
        xored = block ^ prev
        enc = simple_block_encrypt(xored, key)
        ciphertext.append(enc)
        prev = enc
    return ciphertext

def decrypt_cbc(ciphertext_blocks, key, iv):
    plaintext = []
    prev = iv
    for block in ciphertext_blocks:
        dec = simple_block_decrypt(block, key)
        orig = dec ^ prev
        plaintext.append(orig)
        prev = block
    return plaintext

# ------ DEMO ------

key = 0xAABBCCDDEEFF1122
iv  = 0x1234567890ABCDEF

plaintext = [0x1111111111111111, 0x2222222222222222]

cipher = encrypt_cbc(plaintext, key, iv)
print("Ciphertext:", [hex(c) for c in cipher])

decrypted = decrypt_cbc(cipher, key, iv)
print("Decrypted :", [hex(p) for p in decrypted])
