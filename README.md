# Secure File Encryption Tool 🔐

## Project Description
This project implements a secure file encryption system using **hybrid encryption**.
It combines symmetric and asymmetric cryptography to ensure data confidentiality.

- **AES-256** is used to encrypt files
- **RSA-2048** is used to encrypt the AES key

Only users with the RSA private key can decrypt the encrypted file.

---

## Technologies Used
- Python 3
- PyCryptodome
- AES (Advanced Encryption Standard)
- RSA (Public Key Cryptography)
- Kali Linux

---

## Project Structure

---

## Encryption Process
1. An AES-256 key is generated
2. The file is encrypted using AES
3. The AES key is encrypted using the RSA public key
4. The encrypted file and encrypted key are stored securely

---

## Decryption Process
1. The AES key is decrypted using the RSA private key
2. The encrypted file is decrypted using the AES key
3. The original file is restored

---

## How to Run

### Generate RSA keys
```bash
python3 generate_keys.py

## 🖼️ Screenshots

### Step 1: Project Structure
![Project Structure](screenshots/step1_structure.png)

### Step 2: Encrypt the File
![Encrypt](screenshots/step2_encrypt.png)

### Step 3: Decrypt the File
![Decrypt](screenshots/step3_decrypt.png)

### Step 4: Result
![Result](screenshots/step4_result.png)
