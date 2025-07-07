\# Avalanche Effect Analysis Of Static and Dynamic S-Box in AES Encryption



This project explores the Avalanche Effect in AES encryption using two
approaches:  - A \*\*static S-Box\*\* (standard AES implementation)  - A
\*\*dynamic S-Box\*\* generated at runtime using key-dependent or
pseudo-random logic.



The objective is to evaluate and compare the cryptographic diffusion
strength through Avalanche Effect metrics.



\## 🔧 Tools Used - Google Colab - Python (NumPy, matplotlib,
PyCryptodome) - Hamming Distance Analysis - Static & Dynamic S-Box
Design



\## 📊 Features - Custom AES encryption pipeline - Bit-flipping for
Avalanche Effect evaluation - Dynamic S-Box generation logic - Graphical
comparison of avalanche percentages - Statistical output analysis



\## 📁 Project Structure -
\`avalanche_analysis_static_vs_dynamic.ipynb\`: Google Colab Notebook
with code and explanations. - \`dynamic_sbox_module.py\`: Helper file
for dynamic S-Box generation. - \`README.md\`: Project overview and
usage instructions.



\## ▶️ How to Run 1. Open \`avalanche_analysis_static_vs_dynamic.ipynb\`
in \[Google Colab\](https://colab.research.google.com/). 2. Run all
cells sequentially. 3. Review results in console and graphs.


\## 📈 Output Sample


Plaintext: 0x56f50ce8f451792a5a4a38db67174595 Static Cipher:
0x36d5fec8d431590a3a2a18bb47f02575 Dynamic Cipher:
0x30fe895835c1b4db8a52fd151ab52493 Avalanche Effect: Static - 25.78%,
Dynamic - 43.75%



\## 📚 Reference This project was carried out during a vocational
internship at DRDO-ITR Chandipur under guidance of Shri Amit Sardar
(Scientist-F).

\-\--



🔒 \_For educational and research use only.\_
