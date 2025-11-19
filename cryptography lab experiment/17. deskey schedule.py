# ---------------------------------------------------------
#   LEFT ROTATE for 28-bit DES halves
# ---------------------------------------------------------
def left_rotate_28(value, shift):
    return ((value << shift) & 0x0FFFFFFF) | (value >> (28 - shift))


# ---------------------------------------------------------
#   Generate 16 DES subkeys (each 48 bits)
# ---------------------------------------------------------
def generate_des_keys(key56):
    # Split into 28-bit halves
    C = (key56 >> 28) & 0x0FFFFFFF
    D = key56 & 0x0FFFFFFF

    # Standard DES shift schedule
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    subkeys = []

    for s in shifts:
        # Left circular shifts
        C = left_rotate_28(C, s)
        D = left_rotate_28(D, s)

        # First 24 bits from C (drop lower 4 bits)
        C24 = (C >> 4) & 0xFFFFFF

        # Next 24 bits from D (drop lower 4 bits)
        D24 = (D >> 4) & 0xFFFFFF

        # 48-bit subkey
        Ki = (C24 << 24) | D24
        subkeys.append(Ki)

    return subkeys


# ---------------------------------------------------------
#   Reverse order for DECRYPTION keys
# ---------------------------------------------------------
def des_decryption_keys(subkeys):
    return list(reversed(subkeys))


# ---------------------------------------------------------
#   DEMO / TEST
# ---------------------------------------------------------
if __name__ == "__main__":
    key56 = 0x133457799BBCDFF  # Example 56-bit DES key

    print("56-bit Key =", hex(key56))

    # Generate encryption keys
    enc_keys = generate_des_keys(key56)

    print("\n16 Subkeys (Encryption Order):")
    for i, k in enumerate(enc_keys, 1):
        print(f"K{i:2} = {k:012x}")

    # Generate decryption keys
    dec_keys = des_decryption_keys(enc_keys)

    print("\n16 Subkeys (Decryption Order):")
    for i, k in enumerate(dec_keys, 1):
        print(f"K{i:2} = {k:012x}")
