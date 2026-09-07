# Drone & Space Cybersecurity

Hands-on cybersecurity research and laboratory work covering **UAS/drone systems, RF, Software Defined Radio, embedded systems, GNSS, counter-UAS technologies and satellite systems**.

The objective of this repository is to progressively develop practical expertise at the intersection of:

* Cybersecurity
* RF / SDR
* Embedded systems
* Wireless communications
* Robotics
* GNSS / PNT
* Space systems
* Cyber-physical systems

All experiments involving radio transmission, interference or real-world systems are performed only in appropriate, isolated and legally authorized environments.

---

## Objectives

The project aims to develop the ability to:

* Analyze RF signals using SDR
* Understand wireless communication protocols
* Reverse-engineer embedded firmware
* Analyze drone architectures and autopilots
* Assess the security of C2 and telemetry systems
* Understand GNSS and PNT security
* Study RF interference and resilience
* Analyze satellite and ground-segment architectures
* Apply threat modeling to cyber-physical systems
* Design secure communication architectures
* Develop detection and mitigation mechanisms

---

# Roadmap

## Phase 1 — RF & SDR

### 01 — SDR Fundamentals

Topics:

* Frequency
* Wavelength
* Power
* dBm
* Bandwidth
* Noise
* SNR
* Modulation
* IQ samples
* FFT
* Spectrum analysis

Tools:

* RTL-SDR
* SDR++
* GNU Radio
* Python
* NumPy
* SciPy

Status: `⬜`

---

## Phase 2 — Wireless Protocol Security

### 02 — Protocol Security

Topics:

* RF vs protocol layers
* Framing
* Packet structures
* Authentication
* Integrity
* Confidentiality
* Replay attacks
* Sequence numbers
* Nonces
* Key management
* AEAD
* Protocol fuzzing

Project:

Build and progressively secure a custom C2 protocol.

Status: `⬜`

---

## Phase 3 — Embedded Security

### 03 — Embedded Systems

Topics:

* ARM architecture
* Microcontrollers
* Bootloaders
* Flash
* EEPROM
* UART
* SPI
* I²C
* JTAG
* SWD
* Firmware extraction
* Reverse engineering
* Secure Boot
* Firmware signing
* OTA updates
* Hardware Root of Trust

Tools:

* Ghidra
* GDB
* OpenOCD
* binwalk
* Logic analyzer

Status: `⬜`

---

## Phase 4 — Drone Cybersecurity

### 04 — UAS / Drone Security

Topics:

* Drone architecture
* Flight controllers
* Autopilots
* PX4
* ArduPilot
* MAVLink
* Ground Control Stations
* C2
* Telemetry
* Mission protocols
* Sensor security
* Fail-safe mechanisms

Security topics:

* Authentication
* Message integrity
* Replay resistance
* Command injection
* Mission manipulation
* Parameter manipulation
* Ground-station security
* Loss-of-link handling

Primary environment:

* Simulation
* PX4 SITL
* ArduPilot SITL

Status: `⬜`

---

## Phase 5 — GNSS / PNT Security

### 05 — GNSS Security

Topics:

* GPS
* Galileo
* GLONASS
* BeiDou
* GNSS signals
* Pseudorange
* Ephemeris
* Almanac
* Acquisition
* Tracking
* PNT
* Multipath
* RAIM
* Multi-constellation
* Multi-frequency

Security topics:

* GNSS jamming
* GNSS spoofing
* Anomaly detection
* Sensor fusion
* Alternative PNT
* Navigation resilience

Status: `⬜`

---

## Phase 6 — RF Resilience & Counter-UAS

### 06 — RF Resilience

Topics:

* RF interference
* Noise
* Narrowband interference
* Broadband interference
* Spectrum sensing
* Detection
* Filtering
* Frequency hopping
* Spread spectrum
* Directional antennas
* Link monitoring
* Communication resilience
* Navigation resilience

Focus:

**Detection, characterization and mitigation rather than uncontrolled RF interference.**

Status: `⬜`

---

## Phase 7 — Satellite Cybersecurity

### 07 — Space Systems Security

Topics:

### Space Segment

* Satellite architecture
* Flight computer
* Payload
* Telemetry
* Telecommand
* On-board software
* Firmware
* Secure boot
* Key management

### Ground Segment

* Ground stations
* Mission control
* Antennas
* Mission networks
* Authentication
* Access control
* Software infrastructure

### Communication

* TT&C
* Uplink
* Downlink
* Space communications
* CCSDS

Security topics:

* Command authentication
* Replay protection
* Ground-station compromise
* Supply-chain security
* Firmware security
* RF interference
* Availability
* Key management

Status: `⬜`

---

# Final Project — Secure Autonomous Drone Communication System

The final project will combine the knowledge developed throughout the repository.

Proposed architecture:

```text
                    ┌──────────────────┐
                    │  Ground Station  │
                    │                  │
                    │ Mission Control  │
                    └────────┬─────────┘
                             │
                       Authenticated
                       encrypted C2
                             │
                       ┌─────▼─────┐
                       │  RF Link  │
                       └─────┬─────┘
                             │
                      ┌──────▼──────┐
                      │  Autopilot  │
                      │              │
                      │ PX4 / ArduPilot
                      └──────┬──────┘
                             │
                  ┌──────────┼──────────┐
                  │          │          │
                 GNSS       IMU      Barometer
                  │
                  ▼
              Navigation
```

The system will be evaluated against:

* Confidentiality
* Integrity
* Authentication
* Anti-replay
* Key management
* Availability
* RF resilience
* Navigation resilience
* Fail-safe behavior

A complete threat model will be developed using appropriate cybersecurity methodologies.

Status: `⬜`

---

# Laboratory Methodology

Each laboratory follows the same structure:

```text
01 — Objective
02 — Prerequisites
03 — Architecture
04 — Theory
05 — Lab setup
06 — Experiment
07 — Results
08 — Security analysis
09 — Mitigations
10 — Residual risk
11 — References
```

The objective is not only to reproduce a technical result, but to understand:

**why the system behaves that way, how it can fail, and how it can be secured.**

---

# Repository Structure

```text
.
├── 01-sdr/
│   ├── README.md
│   ├── notes/
│   ├── labs/
│   └── scripts/
│
├── 02-protocol-security/
├── 03-embedded/
├── 04-drone/
├── 05-gnss/
├── 06-rf-resilience/
├── 07-satellite/
│
├── 08-final-project/
│
├── docs/
│   ├── glossary.md
│   └── references.md
│
├── .gitignore
└── README.md
```

---

# Progress

| Phase | Subject            | Status |
| ----- | ------------------ | ------ |
| 01    | RF / SDR           | ⬜      |
| 02    | Protocol Security  | ⬜      |
| 03    | Embedded Security  | ⬜      |
| 04    | Drone Security     | ⬜      |
| 05    | GNSS / PNT         | ⬜      |
| 06    | RF Resilience      | ⬜      |
| 07    | Satellite Security | ⬜      |
| 08    | Final Project      | ⬜      |

---

# Principles

* Learn the underlying technology before attacking it.
* Prefer reproducible laboratory environments.
* Use simulation whenever possible.
* Do not interfere with third-party radio systems.
* Document experiments and results.
* Analyze both offensive and defensive perspectives.
* Treat safety and legal constraints as part of the technical design.

---

## Status

**Project started — September 2026**

Phase 1 — **RF / SDR Fundamentals**
