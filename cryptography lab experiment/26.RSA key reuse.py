print("=== RSA Key Reuse Security Checker ===")

# Enter multiple RSA moduli
print("Enter RSA moduli (type 'done' to finish):")

moduli = []
while True:
    value = input("N = ")
    if value.lower() == "done":
        break
    moduli.append(int(value))

print("\nCollected Moduli:")
print(moduli)

# 1. Check for exact duplicates
print("\nChecking for EXACT key reuse...")
duplicates = set([n for n in moduli if moduli.count(n) > 1])

if duplicates:
    print("❌ WARNING: Duplicate RSA modulus found!")
    for d in duplicates:
        print("Modulus reused:", d)
else:
    print("✔ No exact key reuse detected.")

# 2. Check for Common Factor Attack
print("\nChecking for COMMON FACTORS among all moduli...")

for i in range(len(moduli)):
    for j in range(i + 1, len(moduli)):
        a = moduli[i]
        b = moduli[j]

        x = a
        y = b

        # Manual GCD (no functions)
        while y != 0:
            x, y = y, x % y

        gcd_val = x

        if gcd_val != 1:
            print("\n❌ Vulnerability Detected!")
            print("Moduli share a common prime factor!")
            print(f"N{i+1} = {moduli[i]}")
            print(f"N{j+1} = {moduli[j]}")
            print("Common factor p =", gcd_val)

print("\n=== Scan Complete ===")
print("If no warnings appeared above, RSA keys are secure from reuse/common factor attacks.")