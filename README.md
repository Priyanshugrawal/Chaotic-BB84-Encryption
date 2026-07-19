# Chaotic-BB84-Encryption
# Chaotic BB84 Image Encryption using Lorenz System and AES-256

A secure image encryption system that combines **chaotic key generation**, **quantum key distribution**, and **AES-256 encryption**. The project utilizes the Lorenz chaotic system to generate a random binary key, distributes it securely using the BB84 Quantum Key Distribution protocol, derives a 256-bit encryption key using SHA-256, and encrypts images using AES-256 in Counter (CTR) mode.

---

## Overview

Traditional cryptographic systems rely on computational complexity for security. This project integrates concepts from **chaotic systems** and **quantum cryptography** to enhance key generation and key distribution before performing image encryption.

The complete encryption pipeline is:

```
Initial Conditions (x, y, z)
            │
            ▼
Lorenz Chaotic System
            │
            ▼
Chaotic Binary Key
            │
            ▼
BB84 Quantum Key Distribution
            │
            ▼
Sifted Secret Key
            │
            ▼
SHA-256
            │
            ▼
256-bit AES Key
            │
            ▼
AES-256 CTR Image Encryption
            │
            ▼
Encrypted Image
```

---

## Features

- Lorenz Chaotic System based key generation
- Binary key generation using fractional values of X, Y and Z
- XOR-based chaotic bit generation
- BB84 Quantum Key Distribution simulation
- Secure key sifting process
- SHA-256 based AES key derivation
- AES-256 Counter (CTR) Mode image encryption
- Preserves original image dimensions
- Lorenz Time Series visualization
- Lorenz Bifurcation Diagram
- Modular project structure

---

## Project Structure

```
Chaotic-BB84-Encryption/
│
├── BB84/
│   └── bb84.py
│
├── lorenz/
│   ├── __init__.py
│   └── lorenz.py
│
├── lorenz_graph/
│   ├── lorenz1.py
│   ├── lorenz2.py
│   ├── lorenz3.py
│   ├── lorenz4.py
│   ├── lorenz5.py
│   ├── lorenz6.py
│   └── lorenz7.py
│
├── aes_image_encrypt.py
├── main.py
├── README.md
```

---

## Working Principle

### Step 1 : Lorenz Chaotic Key Generation

The Lorenz system generates three chaotic sequences:

- X(t)
- Y(t)
- Z(t)

The standard Lorenz parameters are:

```
σ = 10
ρ = 28
β = 8/3
```

The fractional part of each state variable is converted into binary:

```
Fraction > 0.5  → 1
Fraction ≤ 0.5  → 0
```

The final chaotic bit is obtained by

```
Final Bit = X ⊕ Y ⊕ Z
```

which produces a 1000-bit chaotic binary sequence.

---

### Step 2 : BB84 Quantum Key Distribution

The first 64 bits of the chaotic sequence are used as the input for the BB84 protocol.

The simulation performs

- Random basis generation
- Photon transmission
- Random measurement basis
- Basis comparison
- Sifting process

Only the bits measured using the same basis are retained.

---

### Step 3 : SHA-256 Key Derivation

The sifted BB84 key has variable length.

To generate a fixed-length AES key,

```
AES Key = SHA-256(Sifted Key)
```

which always produces a secure 256-bit encryption key.

---

### Step 4 : AES-256 CTR Image Encryption

The generated AES key encrypts the image using

- AES-256
- Counter (CTR) Mode

CTR mode was selected because

- No padding is required
- Ciphertext length equals plaintext length
- Original image dimensions remain unchanged
- Suitable for image encryption

---

## Lorenz Parameters

| Parameter | Value |
|-----------|-------|
| σ (Sigma) | 10 |
| ρ (Rho) | 28 |
| β (Beta) | 8/3 |
| Time Step | 0.01 |
| Iterations | 1000 |

---

## Graphs Generated

The implementation generates

- Lorenz X(t)
- Lorenz Y(t)
- Lorenz Z(t)
- Lorenz Bifurcation Diagram

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Chaotic-BB84-Encryption.git

cd Chaotic-BB84-Encryption
```

Install dependencies

```bash
pip install numpy matplotlib pillow pycryptodome
```

---

## Running the Project

Execute

```bash
python main.py
```

Provide

- Initial x
- Initial y
- Initial z
- Image path

The program will

1. Generate the chaotic key
2. Perform BB84 key distribution
3. Generate a SHA-256 AES key
4. Encrypt the image

---

## Example Output

```
Enter Initial x : 0.1
Enter Initial y : 0.2
Enter Initial z : 0.3

Chaotic Key Generated

↓

64-bit Key Passed to BB84

↓

Sifted Secret Key

↓

SHA-256 Generated

↓

AES-256 CTR Encryption

↓

encrypted_visual.png
```

---

## Applications

- Secure Image Encryption
- Quantum Cryptography Research
- Chaotic Cryptography
- Secure Key Distribution
- Academic Research
- Educational Demonstration

---

## Future Improvements

- Real Quantum Random Number Generator integration
- Noise simulation
- E91 Quantum Key Distribution
- NIST randomness testing
- Performance evaluation
- Color image encryption analysis
- Histogram analysis
- Correlation analysis
- NPCR and UACI metrics

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Pillow
- PyCryptodome
- SHA-256
- AES-256
- Lorenz Chaotic System
- BB84 Quantum Key Distribution

---

## Author

**Priyanshu Agrawal**

Research & Development Intern

Indian Institute of Space Science and Technology (IIST)

---

## License

This project is intended for educational and research purposes.