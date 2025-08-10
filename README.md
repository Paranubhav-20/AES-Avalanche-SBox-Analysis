# 🔐 Avalanche Effect Analysis of S-Box in 128-bit Encryption

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()
[![AES](https://img.shields.io/badge/Crypto-AES%20128--bit-orange.svg)]()

---

## 📌 Overview
This project investigates the **avalanche effect** in cryptographic systems, focusing on the **Substitution Box (S-Box)** used in **AES 128-bit encryption**.

The avalanche effect ensures that a **small change in input** (like flipping a single bit) causes a **significant change in output** — an essential property for secure encryption.  

We compare **static** and **dynamic** S-Boxes to evaluate their performance in achieving this effect.

---

## 🎯 Objectives
✔ Understand the role of **S-Box** in AES.  
✔ Evaluate the avalanche effect for static vs. dynamic S-Boxes.  
✔ Measure performance in:
- Percentage of bit changes.
- Output randomness.
- Resistance to cryptanalysis.

---

## AES-Avalanche-SBox-Analysis/
│── 📄 README.md                 # Your project documentation
│── 📄 requirements.txt          # Required Python libraries
│── 📄 LICENSE                   # (Optional) License for the repo
│
├── 📁 src                       # Source code files
│   │── 📄 avalanche_analysis.py # Main script to run tests
│   │── 📄 sbox_static.py        # Static S-box related functions
│   │── 📄 sbox_dynamic.py       # Dynamic S-box generation & functions
│   │── 📄 utils.py              # Helper functions (hamming_distance, etc.)
│
├── 📁 plots                     # All generated graphs
│   │── 📊 graph1.png
│   │── 📊 graph2.png
│   │── 📊 graph3.png
│   │── 📊 graph4.png
│
└── 📁 docs                      # Extra documentation (optional)
    │── 📄 report.pdf            # Your detailed analysis report

---

## 🛠️ Technologies Used
- **Language:** Python (Google Colab / Jupyter Notebook)
- **Libraries:**
  - `numpy` – Numerical operations
  - `matplotlib` – Data visualization
- **Concepts:**
  - AES Encryption
  - S-Box Substitution
  - Avalanche Effect Measurement

---

## 📊 Methodology
1. **Generate Input:** Random 128-bit plaintext values.
2. **Encrypt:** Apply both static and dynamic S-Boxes in AES.
3. **Flip Bit:** Change one bit in the plaintext.
4. **Calculate Avalanche Effect:**
   \[
   Avalanche\ Effect = \frac{\text{Number of bits changed}}{\text{Total bits}} \times 100
   \]
5. **Visualize:** Plot avalanche effect results for multiple iterations.

---

## 📈 Results Summary
| S-Box Type  | Average Bit Change | Avalanche Effect |
|-------------|-------------------|------------------|
| Static      | ~50%               | Consistent       |
| Dynamic     | ~50%+              | More unpredictable |

✅ Both maintain strong avalanche properties, ensuring AES security.


<img width="1024" height="1536" alt="Ref Img" src="https://github.com/user-attachments/assets/6fb1056a-2ec7-4609-bb42-e6b3b1538add" />

---

## 📉 Avalanche Effect Process Diagram

![Avalanche Effect Diagram](https://raw.githubusercontent.com/Paranubhav-20/AES-Avalanche-SBox-Analysis/main/plots/avalanche_diagram.png)

---

## 📚 References
- [FIPS PUB 197 – AES Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)
- Daemen, J., & Rijmen, V. *The Design of Rijndael: AES — The Advanced Encryption Standard.*
- Stallings, W. *Cryptography and Network Security.*

---

## 👤 Author
**PARANUBHAV DASH**  
Full-Stack Developer | Cryptography Enthusiast  

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/Paranubhav-20)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/paranubhav26/)
