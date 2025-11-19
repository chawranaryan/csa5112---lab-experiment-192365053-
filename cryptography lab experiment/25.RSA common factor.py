print("=== RSA Common Factor Attack ===")

# Example RSA moduli (N1 and N2 share a common prime factor p)
N1 = int(input("Enter first RSA modulus N1: "))
N2 = int(input("Enter second RSA modulus N2: "))

print("\nCalculating GCD(N1, N2)...")

# Compute GCD
while N2 != 0:
    N1, N2 = N2, N1 % N2
gcd_value = N1

print("GCD =", gcd_value)

if gcd_value == 1:
    print("\nNo common factor found. RSA keys are safe.")
else:
    print("\nCommon prime factor FOUND!")
    print("p =", gcd_value)

    # Recover q for first modulus
    q1 = int(input("\nEnter N1 again to find q (or just type same number): "))
    q1 = q1 // gcd_value

    print("Recovered factors:")
    print("p =", gcd_value)
    print("q =", q1)
    print("\nBoth RSA keys are BROKEN due to shared factor!")