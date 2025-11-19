from Crypto.Util.Padding import pad, unpad

block_size = 8  # DES block size = 8 bytes

plaintext = b"HELLO"
print("Original Plaintext:", plaintext)

# --- Apply PKCS#7 Padding ---
padded = pad(plaintext, block_size)
print("Padded Plaintext (bytes):", padded)
print("Padded Plaintext (hex):", padded.hex())

# --- Remove Padding ---
unpadded = unpad(padded, block_size)
print("After Unpadding:", unpadded)
