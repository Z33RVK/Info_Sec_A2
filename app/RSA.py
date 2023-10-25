from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_RSA_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_key_bytes, public_key_bytes

def encrypt_RSA(public_key, plaintext):
    rsa_key = serialization.load_pem_public_key(public_key)
    ciphertext = rsa_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_RSA(private_key, ciphertext):
    rsa_key = serialization.load_pem_private_key(private_key, password=None)
    plaintext = rsa_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# Example usage:
private_key, public_key = generate_RSA_key()
print("Private key: ",int.from_bytes(private_key, byteorder='big'))
print("Public key: ",int.from_bytes(public_key, byteorder='big'))
plaintext = b"Hello, world!"
ciphertext = encrypt_RSA(public_key, plaintext)
#
print("Ciphertext: ",ciphertext)
decrypted_text = decrypt_RSA(private_key, ciphertext)
print('Decrypted text (raw): ',decrypted_text)
print(decrypted_text.decode())