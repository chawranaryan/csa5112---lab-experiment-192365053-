from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# ----------------------------------------------------
# DES requires:
# - 8-byte key
# - 8-byte block size
# ----------------------------------------------------

key = b"12345678"        # 8 bytes
plaintext = b"HELLO DES ENCRYPTION"

# Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt with padding
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
print("Ciphertext (hex):", ciphertext.hex())

# ----------------------------------------------------
# DECRYPTION
# ----------------------------------------------------

cipher_dec = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher_dec.decrypt(ciphertext), DES.block_size)
print("Decrypted text:", decrypted.decode())
