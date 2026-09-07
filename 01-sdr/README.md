# 01 — SDR Fundamentals

## Objective

Understand the fundamentals of radio-frequency signals and Software Defined Radio (SDR).

The goal of this module is to develop the ability to:

* Understand basic RF concepts
* Read and interpret a spectrum
* Understand frequency, bandwidth and power
* Understand noise and SNR
* Understand I/Q samples
* Record RF data
* Analyze signals using FFT
* Connect RF observations to cybersecurity concepts

---

## Topics

### RF Fundamentals

* Frequency
* Wavelength
* Period
* Amplitude
* Power
* dBm
* Bandwidth
* Noise
* SNR
* Signal propagation

### Digital Signals

* Sampling
* Nyquist-Shannon theorem
* Aliasing
* ADC
* DAC
* I/Q representation
* Complex numbers

### Modulation

* ASK
* FSK
* PSK
* QPSK
* QAM
* OFDM

### SDR

* Software Defined Radio architecture
* RF front-end
* ADC
* Digital signal processing
* SDR receivers
* Spectrum analyzers
* IQ recordings

### Signal Processing

* FFT
* Spectrogram
* Filtering
* Frequency domain
* Time domain
* Sample rate

---

# Laboratory Exercises

## Lab 1.1 — RF Spectrum Observation

**Objective:** Observe and identify RF activity using an SDR.

Status: `⬜`

---

## Lab 1.2 — IQ Capture

**Objective:** Record IQ samples and understand their representation.

Status: `⬜`

---

## Lab 1.3 — FFT Analysis with Python

**Objective:** Process IQ samples using Python and calculate a frequency spectrum.

Status: `⬜`

---

## Lab 1.4 — Signal Characterization

**Objective:** Determine the main characteristics of a recorded signal.

Status: `⬜`

Expected observations:

* Center frequency
* Bandwidth
* Signal power
* Noise floor
* SNR
* Modulation characteristics

Status: `⬜`

---

## Lab 1.5 — Modulation Analysis

**Objective:** Understand and identify basic digital modulation schemes using controlled signals or recordings.

Status: `⬜`

---

# Tools

## Hardware

* SDR receiver
* Antenna
* Computer

## Software

* SDR++
* GNU Radio
* Python
* NumPy
* SciPy
* Matplotlib
* Wireshark (later modules)

---

# Security Relevance

RF analysis is a foundational skill for understanding the security of wireless systems.

The analysis chain used throughout this project can be represented as:

```text
RF Signal
    ↓
IQ Samples
    ↓
Signal Processing
    ↓
Modulation
    ↓
Frame
    ↓
Protocol
    ↓
Packet
    ↓
Command
```

Understanding each layer allows security researchers to analyze wireless systems from the physical layer up to the application layer.

This knowledge will later be applied to:

* Drone C2 systems
* Telemetry links
* GNSS
* Wireless embedded devices
* Satellite communications

---

# Safety

All RF experiments must be performed using legally authorized signals and appropriate laboratory conditions.

Initial laboratories focus on **reception and analysis** rather than RF transmission or interference.

---

# Progress

| Lab | Description             | Status |
| --- | ----------------------- | ------ |
| 1.1 | Spectrum observation    | ⬜      |
| 1.2 | IQ capture              | ⬜      |
| 1.3 | FFT analysis            | ⬜      |
| 1.4 | Signal characterization | ⬜      |
| 1.5 | Modulation analysis     | ⬜      |
