import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Bit sequence
# --------------------------------------------------

BITS = np.array([
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    1, 1
])

# --------------------------------------------------
# QPSK mapping
# --------------------------------------------------

mapping = {
    (0, 0): 45,
    (0, 1): 135,
    (1, 1): 225,
    (1, 0): 315
}

symbols = []

for i in range(0, len(BITS), 2):

    bit_pair = (BITS[i], BITS[i + 1])

    phase_degrees = mapping[bit_pair]
    phase_radians = np.deg2rad(phase_degrees)

    symbol = np.exp(1j * phase_radians)

    symbols.append(symbol)

symbols = np.array(symbols)

# --------------------------------------------------
# Extract I and Q
# --------------------------------------------------

I = np.real(symbols)
Q = np.imag(symbols)

# --------------------------------------------------
# Display symbols
# --------------------------------------------------

print("Bits:")
print(BITS)

print("\nSymbols:")
print(symbols)

print("\nI:")
print(I)

print("\nQ:")
print(Q)

# --------------------------------------------------
# Constellation
# --------------------------------------------------

plt.figure(figsize=(7, 7))

plt.scatter(I, Q, s=100)

plt.axhline(0)
plt.axvline(0)

plt.title("QPSK Constellation")
plt.xlabel("I")
plt.ylabel("Q")

plt.axis("equal")
plt.grid(True)

plt.show()