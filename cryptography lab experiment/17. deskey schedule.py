# --- DES Key Schedule for Decryption (NO def used) ---

# Initial 64-bit key (example key, you can change)
key64 = "0001001100110100010101110111100110011011101111001101111111110001"

# PC-1 Permutation Table (64 → 56 bits)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 (56 → 48 bits)
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Left shift schedule
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# --- Apply PC-1 ---
key56 = ""
for i in PC1:
    key56 += key64[i - 1]

# Split into C0 and D0
C = key56[:28]
D = key56[28:]

round_keys = []

# Generate 16 subkeys for encryption
for r in range(16):
    # left shift C and D
    shift_amount = shifts[r]
    C = C[shift_amount:] + C[:shift_amount]
    D = D[shift_amount:] + D[:shift_amount]
    
    # combine C and D
    CD = C + D

    # Apply PC-2 to get Ki
    Ki = ""
    for j in PC2:
        Ki += CD[j - 1]
    
    round_keys.append(Ki)

print("=== 16 Keys for Encryption (K1 to K16) ===")
for i, k in enumerate(round_keys, start=1):
    print(f"K{i}: {k}")

print("\n=== 16 Keys for Decryption (K16 to K1) ===")
for i, k in enumerate(reversed(round_keys), start=1):
    print(f"K{i}: {k}")