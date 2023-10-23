import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    server_socket.listen(1)
    
    print("Server started. Listening for connections...")
    
    client_socket, client_address = server_socket.accept()
    print("Connection established with:", client_address)
    
    # Step 1: Client Hello
    client_hello = client_socket.recv(1024)
    print("Received Client Hello:", client_hello.decode())
    
    # Step 2: Server Hello
    server_hello = "Server Hello"
    client_socket.sendall(server_hello.encode())
    
    # Step 4: Key Exchange
    shared_key = "Shared Secret Key"
    client_socket.sendall(shared_key.encode())
    
    # Step 6: Handshake Finished
    client_finished = client_socket.recv(1024)
    print("Received Handshake Finished from client:", client_finished.decode())
    
    server_finished = "Handshake Finished"
    client_socket.sendall(server_finished.encode())
    
    # Secure connection established, continue with encrypted communication
    
    # Close the connection
    client_socket.close()

# Start the server
start_server()