class EncryptedSocket:
    """
    Wrapper class for socket that encrypts/decrypts data using a Fernet cipher.
    """

    def __init__(self, socket, cipher):
        self.socket = socket
        self.cipher = cipher

    def sendall(self, data):
        encrypted_data = self.cipher.encrypt(data)
        self.socket.sendall(encrypted_data)

    def recv(self, bufsize):
        encrypted_data = self.socket.recv(bufsize)
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return decrypted_data
