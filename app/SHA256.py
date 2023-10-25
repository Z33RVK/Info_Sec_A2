import hashlib

def hash_SHA256(data):
    sha256_hash = hashlib.sha256(data)
    return sha256_hash.hexdigest()

# Example usage:
data = b"Hello, world!"
hashed_data = hash_SHA256(data)
print("Hashed data: ",hashed_data)
