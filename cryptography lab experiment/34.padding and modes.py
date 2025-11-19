print("=== PKCS#7 Padding (Without Module) ===")

block_size = 8  # DES block size = 8 bytes
plaintext = b"HELLO"

print("Original Plaintext:", plaintext)

# --------- MANUAL PKCS#7 PADDING ----------
pad_len = block_size - (len(plaintext) % block_size)
padded = plaintext + bytes([pad_len] * pad_len)

print("Padded Plaintext (bytes):", padded)
print("Padded Plaintext (hex):", padded.hex())


# --------- MANUAL UNPADDING ----------
last_byte = padded[-1]               # value of last byte
unpadded = padded[:-last_byte]       # remove padding bytes

print("After Unpadding:", unpadded)
