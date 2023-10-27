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
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from flask import Flask, render_template
import EncryptedSocket
import random
from cryptography.hazmat.backends import default_backend
import hashlib

prime = 23
generator = 5

app = Flask(__name__)

def receive_message(client_socket):
    data = client_socket.recv(1024).decode()
    return data

def send_message(client_socket, message):
    client_socket.send(message.encode())


class Server:
    def __init__(self, host, port, certfile, keyfile):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile
        
    def create_server_socket(self):
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Replace with your desired host and port
        server_address = ('localhost', 8282)  
        
        # Bind the socket to a specific host and port
        server_socket.bind(server_address)

        # Return the configured server socket
        return server_socket
            
    def start(self):
        # Server-side implementation

        # Generate a server certificate signed by a trusted CA or self-signed
        server_certificate = self.certfile
        print("1-Setting certificate.")

        # Start listening for incoming connections
        print("2-Setting server socket")
        server_socket = self.create_server_socket()

        server_socket.listen(1)
        print(f"3-listening on localhost:8282")
        client_socket, client_address = server_socket.accept()
        
        # Accept a client connection
        print("Connected to client:", client_address)
        
        # Receive and send messages
        while True:
            received_data = receive_message(client_socket)
            if received_data == 'quit':
                break

            print("Client:", received_data)

            # Process the received data, if needed

            # Send a response
            message = input("You: Enter a message (or 'quit' to exit): ")
            send_message(client_socket, message)
            
            if message == 'quit':
                break


        server_socket.close()
        
        
@app.route('/')
def index():
    return render_template('server.html')


def main():
    
    # Server configuration
    server_host = 'localhost'
    server_port = 1234
    server_certfile = 'server.crt'
    server_keyfile = 'server.key'

    # Start the server
    print("Starting the server")
    server = Server(server_host, server_port, server_certfile, server_keyfile)
    server.start()


if __name__ == '__main__':
    main()
    #app.run(debug=True, port=5000)