from Crypto.Util.number import getRandomRange

def diffie_hellman():
    p = 23  # prime modulus
    g = 5   # generator
    a = getRandomRange(1, p)  # private key for party A
    b = getRandomRange(1, p)  # private key for party B

    A = pow(g, a, p)  # public key for party A
    B = pow(g, b, p)  # public key for party B

    shared_secret_A = pow(B, a, p)  # shared secret for party A
    shared_secret_B = pow(A, b, p)  # shared secret for party B

    return shared_secret_A == shared_secret_B

# Example usage:
shared_secret = diffie_hellman()
print("Shared secret established:", shared_secret)