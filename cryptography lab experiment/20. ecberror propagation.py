# ---------------- CBC ERROR PROPAGATION DEMO ----------------

# XOR function for 8-byte (64-bit) blocks
def xor_block(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

# Simple block encryption (NOT actual DES, only for demo)
# Here crypto = XOR with key for easy demonstration
def encrypt_block(block, key):
    return xor_block(block, key)

def decrypt_block(block, key):
    return xor_block(block, key)

# ------------------------------------------------------------
# CBC ENCRYPTION (2 blocks)

IV = b'\x11\x22\x33\x44\x55\x66\x77\x88'
key = b'\xaa\xbb\xcc\xdd\xee\xff\x10\x20'

P1 = b"ABCDEFGH"  # 8 bytes
P2 = b"IJKLMNOP"  # 8 bytes

# ENC ROUND 1
X1 = xor_block(P1, IV)
C1 = encrypt_block(X1, key)

# ENC ROUND 2
X2 = xor_block(P2, C1)
C2 = encrypt_block(X2, key)

print("Original Ciphertext:")
print("C1 =", C1)
print("C2 =", C2)

# ------------------------------------------------------------
# Introduce 1-bit error in C2
C2_corrupted = bytearray(C2)
C2_corrupted[0] ^= 0x01   # flip lowest bit
C2_corrupted = bytes(C2_corrupted)

print("\nCorrupted C2 (1-bit changed):")
print("C2' =", C2_corrupted)

# ------------------------------------------------------------
# CBC DECRYPTION WITH ERROR

# DEC ROUND 1 (P1 OK)
X1d = decrypt_block(C1, key)
P1d = xor_block(X1d, IV)

# DEC ROUND 2 (P2 corrupted due to C2' change)
X2d = decrypt_block(C2_corrupted, key)
P2d = xor_block(X2d, C1)

# DEC ROUND 3 effect: next block (not present), but if present,
# only 1 byte would be affected

print("\nDecrypted Blocks:")
print("P1' (correct)     =", P1d)
print("P2' (CORRUPTED)  =", P2d)