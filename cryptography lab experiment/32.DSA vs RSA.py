# --------------------------------
# RSA Digital Signature (No Modules)
# --------------------------------

# Key generation (small demo primes)
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)

e = 7            # public exponent
d = 103          # private exponent (modular inverse of e mod phi)

# Simple hash function (since no modules)
def simple_hash(msg):
    h = 0
    for ch in msg:
        h = (h + ord(ch)) % n
    return h

# RSA signing
def rsa_sign(message):
    h = simple_hash(message)
    signature = pow(h, d, n)      # h^d mod n
    return signature

# RSA verification
def rsa_verify(message, signature):
    h = simple_hash(message)
    check = pow(signature, e, n)  # sig^e mod n
    return h == check


# Test
msg = "HELLO"
sig = rsa_sign(msg)

print("RSA Signature:", sig)
print("RSA Verified:", rsa_verify(msg, sig))

