import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    client_socket.connect(server_address)
    
    # Step 1: Client Hello
    client_hello = "Client Hello"
    client_socket.sendall(client_hello.encode())
    
    # Step 2: Server Hello
    server_hello = client_socket.recv(1024)
    print("Received Server Hello:", server_hello.decode())
    
    # Step 4: Key Exchange
    shared_key = client_socket.recv(1024)
    print("Received Shared Key:", shared_key.decode())
    
    # Step 6: Handshake Finished
    client_finished = "Handshake Finished"
    client_socket.sendall(client_finished.encode())
    
    server_finished = client_socket.recv(1024)
    print("Received Handshake Finished from server:", server_finished.decode())
    
    # Secure connection established, continue with encrypted communication
    
    # Close the connection
    client_socket.close()

# Start the client
start_client()