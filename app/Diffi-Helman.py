from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def diffie_hellman():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key_A = parameters.generate_private_key()
    private_key_B = parameters.generate_private_key()

    public_key_A = private_key_A.public_key()
    public_key_B = private_key_B.public_key()

    shared_secret_A = private_key_A.exchange(public_key_B)
    shared_secret_B = private_key_B.exchange(public_key_A)

    return shared_secret_A == shared_secret_B

# Example usage:
shared_secret = diffie_hellman()
print("Shared secret established:", shared_secret)