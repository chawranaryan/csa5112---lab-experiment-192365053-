print("=== Counter Mode (CTR) Encryption ===")

# Get user plaintext (binary blocks separated by space)
plaintext_input = input("Enter plaintext blocks (8-bit each, separated by space): ")
plaintext_blocks = plaintext_input.split()

# Key and counter
key = input("Enter 8-bit key: ")
counter_start = int(input("Enter starting counter (number): "))

print("\nPlaintext blocks:", plaintext_blocks)
print("Key:", key)
print("Counter starts at:", counter_start)

# Helper XOR
def xor(a, b):
    return "".join("0" if a[i] == b[i] else "1" for i in range(len(a)))

ciphertext_blocks = []

print("\n--- CTR Mode Process ---")
for i, P in enumerate(plaintext_blocks):
    counter_value = counter_start + i
    counter_bin = f"{counter_value:08b}"

    encrypted_counter = xor(counter_bin, key)
    C = xor(P, encrypted_counter)

    ciphertext_blocks.append(C)

    print(f"\nBlock {i+1}:")
    print("  Counter:        ", counter_bin)
    print("  E(K, Counter):  ", encrypted_counter)
    print("  Ciphertext:", C)

print("\nFinal Ciphertext:")
print(" ".join(ciphertext_blocks))

print("\nAdvantages of CTR Mode:")
print("- Parallel encryption")
print("- Random access to blocks")
print("- No error propagation")