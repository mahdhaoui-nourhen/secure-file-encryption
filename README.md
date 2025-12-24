# Secure File Encryption Tool 🔐

## Project Description
This project implements a secure file encryption system using **hybrid encryption**.
It combines symmetric and asymmetric cryptography to ensure data confidentiality.

- **AES-256** is used to encrypt files
- **RSA-2048** is used to encrypt the AES key

Only users with the RSA private key can decrypt the encrypted file.

---

## Technologies Used
 **Python 3**: Main programming language.
- **PyCryptodome**: Cryptography library for AES and RSA.
- **AES (Advanced Encryption Standard)**: For fast and secure symmetric encryption.
- **RSA (Public Key Cryptography)**: For secure asymmetric encryption of AES keys.
- **Kali Linux**: Development and testing environment.

---

## Encryption Process
The encryption process uses **AES-256 in EAX mode** for strong symmetric encryption and **RSA (2048-bit)** to securely encrypt the AES key.  

Steps:
1. Generate a **random 256-bit AES key**.
2. Encrypt the original file (`sample.txt`) using AES.
3. Encrypt the AES key using the **RSA public key**.
4. Save the **encrypted file** (`sample.enc`) and **encrypted AES key** (`keys/aes_key.enc`).

> This hybrid encryption ensures that even if the encrypted file is stolen, without the RSA private key, the content cannot be decrypted.

---

## Decryption Process
Decryption restores the original file using the following steps:

1. Load the **RSA private key** from `keys/private.pem`.
2. Decrypt the **AES key** using the RSA private key.
3. Decrypt the **encrypted file** (`sample.enc`) using the AES key.
4. Save the decrypted content to `sample_decrypted.txt`.

> Only authorized users with the private key can decrypt and access the original content.

---

---

## How to Run

### Generate RSA keys
```bash
python3 generate_keys.py
👩‍💻 Author

Secure File Encryption Project
Developed by: mahdhaoui nourhen

📝 Conclusion

This Secure File Encryption System demonstrates a practical implementation of hybrid cryptography, combining the speed of AES-256 with the security of RSA asymmetric encryption.

Key takeaways:

Confidentiality: Sensitive data is protected at rest and in transit.

Security: AES key is never exposed; only RSA private key can decrypt it.

Usability: Scripts are simple, modular, and easy to run in any Python 3 environment.

Scalability: This framework can be extended to encrypt multiple files, integrate with user authentication, or incorporate additional security layers.

By following best practices in cryptography and software organization, this project provides a robust and professional encryption solution, suitable for academic demonstration, secure personal storage, or integration into larger systems requiring data security.

📌 References

PyCryptodome Documentation

AES Encryption

RSA Encryption
