from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_AES(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_AES(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example usage:
key = get_random_bytes(16)  # 128-bit key
plaintext = b"Hello, world!"
ciphertext = encrypt_AES(key, plaintext)
decrypted_text = decrypt_AES(key, ciphertext)
print(decrypted_text.decode())