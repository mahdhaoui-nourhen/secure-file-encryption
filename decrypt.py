from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

# Load encrypted AES key
with open("keys/aes_key.enc", "rb") as f:
    encrypted_aes_key = f.read()

# Load private RSA key
with open("keys/private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Load encrypted file
with open("sample.enc", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

# Decrypt file
cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

with open("sample_decrypted.txt", "wb") as f:
    f.write(data)

print("File decrypted successfully.")
