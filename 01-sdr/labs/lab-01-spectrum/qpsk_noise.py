import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Parameters
# --------------------------------------------------

"""BITS = np.array([
    0, 0,
    0, 1,
    1, 1,
    1, 0,
    0, 0,
    1, 1
])"""

NUM_BITS = 10000

BITS = np.random.randint(
    0,
    2,
    NUM_BITS
)

SNR_DB = 10

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
# Add AWGN noise
# --------------------------------------------------

signal_power = np.mean(np.abs(symbols) ** 2)

snr_linear = 10 ** (SNR_DB / 10)

noise_power = signal_power / snr_linear

noise = np.sqrt(noise_power / 2) * (
    np.random.randn(len(symbols))
    + 1j * np.random.randn(len(symbols))
)

received_symbols = symbols + noise

# --------------------------------------------------
# Extract I/Q
# --------------------------------------------------

I = np.real(received_symbols)
Q = np.imag(received_symbols)

# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(7, 7))

plt.scatter(I, Q, s=100)

plt.axhline(0)
plt.axvline(0)

plt.title(f"QPSK Constellation - SNR = {SNR_DB} dB")
plt.xlabel("I")
plt.ylabel("Q")

plt.axis("equal")
plt.grid(True)

plt.show()