from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Read original file
with open("sample.txt", "rb") as f:
    data = f.read()

# Generate AES key (256 bits)
aes_key = get_random_bytes(32)

# Encrypt file with AES
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

with open("sample.enc", "wb") as f:
    f.write(cipher_aes.nonce + tag + ciphertext)

# Encrypt AES key using RSA public key
with open("keys/public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

with open("keys/aes_key.enc", "wb") as f:
    f.write(encrypted_aes_key)

print("File encrypted successfully.")
