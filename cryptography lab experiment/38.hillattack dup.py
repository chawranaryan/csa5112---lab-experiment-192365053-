import numpy as np

print("=== Hill Cipher Attack (2x2) ===")

# ---- Known plaintext-ciphertext pairs ----
# Duplicate characters included intentionally

plaintext = "HELP"
ciphertext = "ZEBB"

# Convert letters to numbers (A=0,...Z=25)
P = [(ord(c) - 65) for c in plaintext]
C = [(ord(c) - 65) for c in ciphertext]

# Create 2x2 matrices using pairs (duplicated allowed)
P_matrix = np.array([[P[0], P[1]],
                     [P[2], P[3]]])

C_matrix = np.array([[C[0], C[1]],
                     [C[2], C[3]]])

print("Plaintext Matrix:\n", P_matrix)
print("Ciphertext Matrix:\n", C_matrix)

# ---- Invert plaintext matrix mod 26 ----
det = int(np.round(np.linalg.det(P_matrix)))
det_mod = det % 26

# Find modular inverse of determinant mod 26
def inverse_mod(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None

det_inv = inverse_mod(det_mod, 26)
if det_inv is None:
    print("Matrix not invertible mod 26!")
    exit()

# Adjoint of plaintext matrix
adj = np.round(det * np.linalg.inv(P_matrix)).astype(int) % 26

# Compute inverse mod 26
P_inv = (det_inv * adj) % 26

print("Inverse of Plaintext Matrix (mod 26):\n", P_inv)

# ---- Recover Key K ----
K = (C_matrix.dot(P_inv)) % 26
print("Recovered Key Matrix K:\n", K)

# ---- Verify ----
test = (K.dot(P_matrix)) % 26
print("Verification (K * P mod 26):\n", test)
