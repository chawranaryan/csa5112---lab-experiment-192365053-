# DES Subkey Generation (K1–K16)

# PC-1 (64 → 56 bits)
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


# ---- Generate 16 DES Subkeys ----
def generate_des_subkeys(key64):
    # Apply PC-1
    key56 = "".join(key64[i - 1] for i in PC1)

    # Split into C0 and D0
    C = key56[:28]
    D = key56[28:]

    round_keys = []

    # Generate 16 keys
    for r in range(16):
        # Left shifts
        shift_val = shifts[r]
        C = C[shift_val:] + C[:shift_val]
        D = D[shift_val:] + D[:shift_val]

        # Combine
        CD = C + D

        # Apply PC-2 → 48-bit key
        K = "".join(CD[i - 1] for i in PC2)
        round_keys.append(K)

    return round_keys


# Example 64-bit key
key64 = "0001001100110100010101110111100110011011101111001101111111110001"

subkeys = generate_des_subkeys(key64)

print("=== DES Subkeys (K1–K16) ===")
for i, k in enumerate(subkeys, start=1):
    print(f"K{i}: {k}")