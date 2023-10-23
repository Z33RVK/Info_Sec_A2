from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_RSA_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_RSA(public_key, plaintext):
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher_rsa.encrypt(plaintext)
    return ciphertext

def decrypt_RSA(private_key, ciphertext):
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext

# Example usage:
private_key, public_key = generate_RSA_key()
plaintext = b"Hello, world!"
ciphertext = encrypt_RSA(public_key, plaintext)
decrypted_text = decrypt_RSA(private_key, ciphertext)
print(decrypted_text.decode())