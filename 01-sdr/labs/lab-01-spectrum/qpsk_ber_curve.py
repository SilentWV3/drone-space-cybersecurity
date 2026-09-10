import numpy as np
import matplotlib.pyplot as plt

NUM_BITS = 1_000_000
SNR_VALUES = [20, 15, 10, 5, 0, -5]

mapping = {
    (0, 0): 45,
    (0, 1): 135,
    (1, 1): 225,
    (1, 0): 315
}

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


def qpsk_modulate(bits):
    bit_pairs = bits.reshape(-1, 2)

    symbols = []

    for pair in bit_pairs:
        phase = np.deg2rad(mapping[tuple(pair)])
        symbols.append(np.exp(1j * phase))

    return np.array(symbols)


def qpsk_demodulate(symbols):
    bits = []

    for symbol in symbols:
        distances = np.abs(symbol - constellation)
        closest_index = np.argmin(distances)
        bits.extend(constellation_bits[closest_index])

    return np.array(bits)


bits_tx = np.random.randint(0, 2, NUM_BITS)

if len(bits_tx) % 2 != 0:
    bits_tx = bits_tx[:-1]

symbols_tx = qpsk_modulate(bits_tx)

ber_results = []

for snr_db in SNR_VALUES:

    signal_power = np.mean(np.abs(symbols_tx) ** 2)

    snr_linear = 10 ** (snr_db / 10)

    noise_power = signal_power / snr_linear

    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(len(symbols_tx))
        + 1j * np.random.randn(len(symbols_tx))
    )

    symbols_rx = symbols_tx + noise

    bits_rx = qpsk_demodulate(symbols_rx)

    bit_errors = np.sum(bits_tx != bits_rx)

    ber = bit_errors / len(bits_tx)

    ber_results.append(ber)

    print(
        f"SNR = {snr_db:>3} dB | "
        f"Errors = {bit_errors:>6} | "
        f"BER = {ber:.6f}"
    )


plt.figure(figsize=(8, 6))

plt.semilogy(SNR_VALUES, ber_results, marker="o")

plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("QPSK BER vs SNR")

plt.grid(True, which="both")
plt.show()