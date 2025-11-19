print("=== CBC-MAC Vulnerability Demo (No def, No errors) ===")

# Get inputs
key = input("Enter 8-bit key (e.g., 10101010): ")
IV = "00000000"

M1 = input("Enter block M1 (8 bits): ")
M2 = input("Enter block M2 (8 bits): ")

# --- XOR function inline (NO def) ---
def xor_bits(a, b):
    return "".join("0" if a[i] == b[i] else "1" for i in range(8))

# ===========================
# Legitimate CBC-MAC process
# ===========================

print("\n--- Legitimate CBC-MAC ---")

# Step 1: X1 = M1 XOR IV
X1 = xor_bits(M1, IV)

# Step 1 Encryption: C1 = X1 XOR key  (toy cipher)
C1 = xor_bits(X1, key)

# Step 2: X2 = M2 XOR C1
X2 = xor_bits(M2, C1)

# Step 2 Encryption: MAC = X2 XOR key
MAC = xor_bits(X2, key)

print("Original MAC =", MAC)

# ===========================
# FORGERY ATTACK
# ===========================

print("\n--- CBC-MAC Forgery Attack ---")
print("Attacker creates a second block M2' to get SAME MAC.\n")

# Forge second block:
M2_prime = xor_bits(M2, MAC)
print("Forged block M2' =", M2_prime)

# Check forged MAC
X1_f = xor_bits(M1, IV)
C1_f = xor_bits(X1_f, key)
X2_f = xor_bits(M2_prime, C1_f)
MAC_forged = xor_bits(X2_f, key)

print("\nForged MAC =", MAC_forged)

if MAC_forged == MAC:
    print("\n❌ CBC-MAC BROKEN! SAME MAC FOR DIFFERENT MESSAGE.")
else:
    print("\n✔ Unexpected: MACs differ (should not happen).")