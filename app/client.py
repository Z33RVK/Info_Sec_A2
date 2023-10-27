# Import necessary libraries
import socket
import ssl
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hmac
from cryptography.fernet import Fernet
from flask import Flask, render_template
import os
import datetime
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import EncryptedSocket
from cryptography.hazmat.backends import default_backend

prime = 23
generator = 5

app = Flask(__name__)

def receive_message(client_socket):
    data = client_socket.recv(1024).decode()
    return data

def send_message(client_socket, message):
    client_socket.send(message.encode())


class Client:
    def __init__(self, host, port, certfile, data):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.data = data


    def generate_client_certificate(self, host, port, certfile):
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        # Create a certificate signing request (CSR)
        csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, host),
        ])).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(host),
                x509.DNSName(f"localhost:{port}")
            ]),
            critical=False
        ).sign(private_key, hashes.SHA256(), default_backend())

        # Generate a self-signed certificate
        certificate = x509.CertificateBuilder().subject_name(csr.subject).issuer_name(csr.subject).public_key(
            csr.public_key()).serial_number(x509.random_serial_number()).not_valid_before(
            datetime.datetime.utcnow()).not_valid_after(
            datetime.datetime.utcnow() + datetime.timedelta(days=365)).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(host),
                x509.DNSName(f"localhost:{port}")
            ]),
            critical=False
        ).sign(private_key, hashes.SHA256(), default_backend())

        # Save the private key and certificate to files
        with open(certfile, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
            f.write(certificate.public_bytes(serialization.Encoding.PEM))

        # Return the private key and certificate as bytes
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        certificate_bytes = certificate.public_bytes(serialization.Encoding.PEM)
        return private_key_bytes, certificate_bytes

    def create_client_socket(self):
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        return server_socket

    def connect(self):
        # Client-side implementation

        # Generate a client certificate signed by a trusted CA or self-signed
        print("1-Generating client certificate.")
        client_certificate = self.generate_client_certificate(self.host,self.port,self.certfile)

        # Connect to the server
        print("2-Creating the client socket")
        client_socket = self.create_client_socket()
        # connect to the server
        # Replace with your desired host and port
        server_address = ('localhost', 8282)  
        
        # Bind the socket to a specific host and port
        client_socket.connect(server_address)

        print("Connected to server:", server_address)
        
        # Send and receive messages
        while True:
            message = input("You: Enter a message (or 'quit' to exit): ")
            send_message(client_socket, message)

            if message == 'quit':
                break

            received_data = receive_message(client_socket)
            print("Server: ", received_data)
            
            if receive_message == 'quit':
                break

        client_socket.close()

def main():
    # Client configuration
    client_host = 'localhost'
    client_port = 1234
    client_certfile = 'client.crt'
    client_message = 'hello'

    # Connect the client
    print("Starting the client")
    client = Client(client_host, client_port, client_certfile, client_message)
    client.connect()
    

@app.route('/')
def index():
    return render_template('client.html')


if __name__ == '__main__':
    main()
    #app.run(debug=True, port=5001)