# -------------------------------------------------------
#    DES KEY SCHEDULE: 28-bit C, 28-bit D, 48-bit subkeys
#    - No external libraries
#    - First 24 bits from C
#    - Next 24 bits from D
# -------------------------------------------------------

# Left rotation of n-bit value
def left_rotate(value, shift, bits):
    return ((value << shift) & ((1 << bits) - 1)) | (value >> (bits - shift))


# Generate 16 DES subkeys (48-bit)
def generate_des_subkeys(key_56):
    # Split into two 28-bit halves
    C = (key_56 >> 28) & 0x0FFFFFFF
    D = key_56 & 0x0FFFFFFF

    # Standard DES shift schedule
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    subkeys = []

    for i in range(16):
        # Left-shift both halves
        C = left_rotate(C, shifts[i], 28)
        D = left_rotate(D, shifts[i], 28)

        # FIRST 24 bits from C (drop lower 4 bits)
        C24 = (C >> 4) & 0xFFFFFF

        # NEXT 24 bits from D (drop lower 4 bits)
        D24 = (D >> 4) & 0xFFFFFF

        # 48-bit round key = 24 bits from C || 24 bits from D
        Ki = (C24 << 24) | D24
        subkeys.append(Ki)

    return subkeys


# -------------------------
# TEST
# -------------------------
key_56 = 0x133457799BBCDFF  # 56-bit key example

print("KEY (56-bit) =", hex(key_56))
print("\nGenerated 16 Subkeys:\n")

subkeys = generate_des_subkeys(key_56)

for i, k in enumerate(subkeys, 1):
    print(f"Round {i:2}: {k:012x}")  # 48-bit = 12 hex digits
