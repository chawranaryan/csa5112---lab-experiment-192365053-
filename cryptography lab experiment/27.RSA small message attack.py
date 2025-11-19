print("=== RSA Small Message Attack ===")

# Public exponent (small e)
e = int(input("Enter public exponent e (use 3 or 5): "))

# RSA modulus N
N = int(input("Enter RSA modulus N: "))

# Ciphertext C
C = int(input("Enter ciphertext C: "))

print("\nChecking vulnerability...")
print("If m^e < N, RSA encryption is NOT secure.")

# Find integer e-th root
m = int(C ** (1.0 / e))

print("\nRecovered message (approx):", m)

# Verify:
print("Verification: m^e =", m ** e)

if m ** e == C:
    print("\n❌ RSA BROKEN! Small message attack successful.")
else:
    print("\n✔ Not vulnerable (m^e >= N).")