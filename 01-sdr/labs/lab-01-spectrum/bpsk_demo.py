import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Parameters
# --------------------------------------------------

BITS = np.array([1, 0, 1, 1, 0, 0, 1, 0])

# --------------------------------------------------
# BPSK modulation
# --------------------------------------------------

symbols = []

for bit in BITS:

    if bit == 1:
        symbol = 1 + 0j
    else:
        symbol = -1 + 0j

    symbols.append(symbol)

symbols = np.array(symbols)

# --------------------------------------------------
# Extract I and Q
# --------------------------------------------------

I = np.real(symbols)
Q = np.imag(symbols)

# --------------------------------------------------
# Plot constellation
# --------------------------------------------------

plt.figure(figsize=(7, 7))

plt.scatter(I, Q, s=100)

plt.title("BPSK Constellation")
plt.xlabel("I")
plt.ylabel("Q")

plt.axis("equal")
plt.grid(True)

plt.show()