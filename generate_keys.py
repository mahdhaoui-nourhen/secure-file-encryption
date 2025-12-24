from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

# Save private key
with open("keys/private.pem", "wb") as f:
    f.write(private_key)

# Save public key
with open("keys/public.pem", "wb") as f:
    f.write(public_key)

print("RSA keys generated successfully.")
