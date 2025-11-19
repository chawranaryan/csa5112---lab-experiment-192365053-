print("=== SHA-3 State Propagation Demo ===")

# 5x5 mini-state (each lane is 8-bit instead of 64-bit, for simplicity)
state = [
    [0x01, 0x02, 0x03, 0x04, 0x05],
    [0x10, 0x20, 0x30, 0x40, 0x50],
    [0xAA, 0xBB, 0xCC, 0xDD, 0xEE],
    [0x11, 0x22, 0x33, 0x44, 0x55],
    [0xFF, 0xEE, 0xDD, 0xCC, 0xBB]
]

print("\nInitial State (5x5):")
for row in state:
    print([hex(x) for x in row])

# Introduce a 1-bit change
print("\nFlipping 1 bit in state[0][0] ...")
state[0][0] ^= 0x01   # Flip lowest bit

print("\nState After 1-bit Change:")
for row in state:
    print([hex(x) for x in row])

# SHA-3 like round (Theta + Rho + Pi + Chi approximation)
print("\n--- Propagating Through One Round ---")

# Theta: XOR each lane with column parity
column_parity = [0, 0, 0, 0, 0]
for x in range(5):
    for y in range(5):
        column_parity[x] ^= state[y][x]

for x in range(5):
    for y in range(5):
        state[y][x] ^= column_parity[(x - 1) % 5]

# Rho: rotate each lane by (x+y) bits (small rotation simulated)
for x in range(5):
    for y in range(5):
        rot = (x + y) % 8
        val = state[y][x]
        state[y][x] = ((val << rot) & 0xFF) | (val >> (8 - rot))

# Chi: nonlinear substitution
for y in range(5):
    new_row = [0]*5
    for x in range(5):
        new_row[x] = state[y][x] ^ ((~state[y][(x+1)%5]) & state[y][(x+2)%5])
    state[y] = new_row

print("\nState After One Keccak-like Round:")
for row in state:
    print([hex(x) for x in row])