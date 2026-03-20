import socket

def server_program():
    # Get the hostname (use 0.0.0.0 to listen on all available interfaces)
    host = '0.0.0.0'
    port = 6000  # Initiate port number above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2) # Configure how many clients the server can listen to simultaneously

    print(f"Server listening on {host}:{port}...")

    conn, address = server_socket.accept() # Accept new connection
    print(f"Connection from: {str(address)}")

    while True:
        # Receive data stream (up to 1024 bytes)
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"From connected user: {str(data)}")

        # Send response to the client
        message = input(' -> ')
        conn.send(message.encode())

    conn.close() # Close the connection

if __name__ == '__main__':
    server_program()
