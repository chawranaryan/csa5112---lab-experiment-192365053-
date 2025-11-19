from Crypto.Cipher import AES

# Left shift a 16-byte block
def left_shift(b):
    shifted = int.from_bytes(b, "big") << 1
    return (shifted & (2**128 - 1)).to_bytes(16, "big")

# XOR last byte with Rb (AES polynomial)
def xor_rb(b):
    rb = 0x87
    return b[:-1] + bytes([b[-1] ^ rb])

print("=== CMAC Subkey Generation ===")

# Input 16-byte AES key
key_hex = input("Enter 128-bit AES key (32 hex chars): ")
key = bytes.fromhex(key_hex)

# AES encrypt 0…0 block to get L
zero_block = bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
L = cipher.encrypt(zero_block)

print("\nL =", L.hex())

# Generate K1
if (L[0] & 0x80) == 0:   # MSB = 0
    K1 = left_shift(L)
else:
    K1 = xor_rb(left_shift(L))

print("K1 =", K1.hex())

# Generate K2
if (K1[0] & 0x80) == 0:
    K2 = left_shift(K1)
else:
    K2 = xor_rb(left_shift(K1))

print("K2 =", K2.hex())
