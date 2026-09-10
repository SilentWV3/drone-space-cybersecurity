import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Parameters
# --------------------------------------------------

NUM_BITS = 10000
SNR_DB = 10 # 0, 5, 10, 20

# --------------------------------------------------
# Generate random bits
# --------------------------------------------------

bits_tx = np.random.randint(0, 2, NUM_BITS)

# Make sure we have an even number of bits
if len(bits_tx) % 2 != 0:
    bits_tx = bits_tx[:-1]

# --------------------------------------------------
# Group bits into pairs
# --------------------------------------------------

bit_pairs = bits_tx.reshape(-1, 2)

# --------------------------------------------------
# QPSK mapping
# Gray mapping:
#
# 00 -> 45°
# 01 -> 135°
# 11 -> 225°
# 10 -> 315°
# --------------------------------------------------

mapping = {
    (0, 0): 45,
    (0, 1): 135,
    (1, 1): 225,
    (1, 0): 315
}

symbols_tx = []

for pair in bit_pairs:
    phase = np.deg2rad(mapping[tuple(pair)])
    symbol = np.exp(1j * phase)
    symbols_tx.append(symbol)

symbols_tx = np.array(symbols_tx)

# --------------------------------------------------
# Add AWGN
# --------------------------------------------------

signal_power = np.mean(np.abs(symbols_tx) ** 2)

snr_linear = 10 ** (SNR_DB / 10)

noise_power = signal_power / snr_linear

noise = np.sqrt(noise_power / 2) * (
    np.random.randn(len(symbols_tx))
    + 1j * np.random.randn(len(symbols_tx))
)

symbols_rx = symbols_tx + noise

# --------------------------------------------------
# Decision: find closest QPSK symbol
# --------------------------------------------------

constellation = np.array([
    np.exp(1j * np.deg2rad(45)),
    np.exp(1j * np.deg2rad(135)),
    np.exp(1j * np.deg2rad(225)),
    np.exp(1j * np.deg2rad(315))
])

constellation_bits = [
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 0)
]

bits_rx = []

for symbol in symbols_rx:

    distances = np.abs(symbol - constellation)

    closest_index = np.argmin(distances)

    bits_rx.extend(
        constellation_bits[closest_index]
    )

bits_rx = np.array(bits_rx)

# --------------------------------------------------
# Calculate BER
# --------------------------------------------------

bit_errors = np.sum(bits_tx != bits_rx)

ber = bit_errors / len(bits_tx)

print("SNR:", SNR_DB, "dB")
print("Total bits:", len(bits_tx))
print("Bit errors:", bit_errors)
print("BER:", ber)

# --------------------------------------------------
# Plot constellation
# --------------------------------------------------

plt.figure(figsize=(7, 7))

plt.scatter(
    np.real(symbols_rx),
    np.imag(symbols_rx),
    s=5
)

plt.scatter(
    np.real(constellation),
    np.imag(constellation),
    s=100
)

plt.axhline(0)
plt.axvline(0)

plt.title(f"QPSK - SNR = {SNR_DB} dB - BER = {ber:.4f}")

plt.xlabel("I")
plt.ylabel("Q")

plt.axis("equal")
plt.grid(True)

plt.show()