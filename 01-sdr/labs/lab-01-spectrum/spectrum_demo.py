import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Configuration
# ============================================================

SAMPLE_RATE = 10e6       # 10 MHz
SIGNAL_FREQ = 1e6        # 1 MHz
DURATION = 0.001         # 1 ms
NOISE_LEVEL = 0.3


# ============================================================
# Generate time samples
# ============================================================

num_samples = int(SAMPLE_RATE * DURATION)

time = np.arange(num_samples) / SAMPLE_RATE


# ============================================================
# Generate RF signal
# ============================================================

signal = np.sin(2 * np.pi * SIGNAL_FREQ * time)


# ============================================================
# Add Gaussian noise
# ============================================================

noise = NOISE_LEVEL * np.random.randn(num_samples)

received_signal = signal + noise


# ============================================================
# FFT
# ============================================================

spectrum = np.fft.fft(received_signal)
frequencies = np.fft.fftfreq(num_samples, 1 / SAMPLE_RATE)


# Shift zero frequency to the center

spectrum = np.fft.fftshift(spectrum)
frequencies = np.fft.fftshift(frequencies)


# Convert magnitude to dB

magnitude = np.abs(spectrum)

magnitude_db = 20 * np.log10(magnitude + 1e-12)


# ============================================================
# Plot
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    frequencies / 1e6,
    magnitude_db
)

plt.title("Simulated RF Spectrum")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

plt.tight_layout()
plt.show()