"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters
SAMPLE_RATE = 10e6
SIGNAL_FREQ = 1e6
DURATION = 0.001

# Number of samples
num_samples = int(SAMPLE_RATE * DURATION)

# Time vector
time = np.arange(num_samples) / SAMPLE_RATE

# --------------------------------------------------
# 1. Real signal
# --------------------------------------------------

real_signal = np.sin(2 * np.pi * SIGNAL_FREQ * time)

real_spectrum = np.fft.fft(real_signal)
frequencies = np.fft.fftfreq(num_samples, 1 / SAMPLE_RATE)

real_spectrum = np.fft.fftshift(real_spectrum)
frequencies = np.fft.fftshift(frequencies)

real_magnitude_db = 20 * np.log10(
    np.abs(real_spectrum) + 1e-12
)

# --------------------------------------------------
# 2. Complex signal / I-Q
# --------------------------------------------------

complex_signal = np.exp(
    1j * 2 * np.pi * SIGNAL_FREQ * time
)

complex_spectrum = np.fft.fft(complex_signal)

complex_spectrum = np.fft.fftshift(complex_spectrum)

complex_magnitude_db = 20 * np.log10(
    np.abs(complex_spectrum) + 1e-12
)

# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)

plt.plot(
    frequencies / 1e6,
    real_magnitude_db
)

plt.title("Real Signal")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

plt.subplot(2, 1, 2)

plt.plot(
    frequencies / 1e6,
    complex_magnitude_db
)

plt.title("Complex Signal / I-Q")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

plt.tight_layout()
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
SAMPLE_RATE = 10e6
SIGNAL_FREQ = 1e6
DURATION = 0.00001

# Time
num_samples = int(SAMPLE_RATE * DURATION)
time = np.arange(num_samples) / SAMPLE_RATE

# I/Q components
I = np.cos(2 * np.pi * SIGNAL_FREQ * time)
Q = np.sin(2 * np.pi * SIGNAL_FREQ * time)

# Complex signal
signal = I + 1j * Q

# --------------------------------------------------
# Time domain
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(time * 1e6, I, label="I")
plt.plot(time * 1e6, Q, label="Q")

plt.title("I/Q Components")
plt.xlabel("Time (µs)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# --------------------------------------------------
# I/Q plane
# --------------------------------------------------

plt.figure(figsize=(7, 7))

plt.plot(I, Q)

plt.title("I/Q Plane")
plt.xlabel("I")
plt.ylabel("Q")

plt.axis("equal")
plt.grid(True)

plt.tight_layout()
plt.show()