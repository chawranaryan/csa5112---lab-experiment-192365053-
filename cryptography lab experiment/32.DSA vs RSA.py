from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pkcs1_15, DSS
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# -----------------------------
# Message
# -----------------------------
message = b"Cryptography Signature Test"
h = SHA256.new(message)

# ======================================================
#                  RSA SIGNATURE
# ======================================================

# Generate RSA key pair
rsa_key = RSA.generate(2048)
rsa_public = rsa_key.publickey()

# RSA Sign
rsa_signature = pkcs1_15.new(rsa_key).sign(h)
print("RSA Signature:", rsa_signature.hex())

# RSA Verify
try:
    pkcs1_15.new(rsa_public).verify(h, rsa_signature)
    print("[RSA] Signature Verified Successfully")
except:
    print("[RSA] Signature Verification Failed")

# ======================================================
#                  DSA SIGNATURE
# ======================================================

# Generate DSA key pair
dsa_key = DSA.generate(2048)
dsa_public = dsa_key.publickey()

# DSA Sign
dsa_signature = DSS.new(dsa_key, 'fips-186-3').sign(h)
print("\nDSA Signature:", dsa_signature.hex())

# DSA Verify
try:
    DSS.new(dsa_public, 'fips-186-3').verify(h, dsa_signature)
    print("[DSA] Signature Verified Successfully")
except:
    print("[DSA] Signature Verification Failed")
