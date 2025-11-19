# ---------------- BLOCK CIPHER DEMO ----------------
# Block size = 8 bytes (like DES)

BLOCK_SIZE = 8

# Example plaintext that does NOT fit evenly into 8 bytes
plaintext = b"HELLO WORLD"   # 11 bytes

print("Plaintext:", plaintext)
print("Length:", len(plaintext))


# ---------------- WHY WE NEED PADDING ----------------
print("\n=== Trying to split into 8-byte blocks (without padding) ===")

blocks = [plaintext[i:i+BLOCK_SIZE] for i in range(0, len(plaintext), BLOCK_SIZE)]
for i, b in enumerate(blocks, 1):
    print(f"Block {i}:", b)

print("\nNotice Block 2 is NOT full (only 3 bytes).")
print("A block cipher CANNOT encrypt this block!")
print("This is why padding is required.\n")


# ---------------- ADD PADDING (PKCS#7) ----------------
padding_len = BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)
padding = bytes([padding_len]) * padding_len

padded_plaintext = plaintext + padding

print("=== Padded Plaintext ===")
print(padded_plaintext)
print("Length:", len(padded_plaintext))


# Splitting padded text
padded_blocks = [padded_plaintext[i:i+BLOCK_SIZE] for i in range(0, len(padded_plaintext), BLOCK_SIZE)]
print("\nBlocks after padding:")
for i, b in enumerate(padded_blocks, 1):
    print(f"Block {i}:", b)

print("\nNow all blocks are FULL → encryption is possible.")