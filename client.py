import socket

def client_program():
    # Set the server's IP address and port
    # Use the server's actual IP address if on different machines
    host = '127.0.0.1' # Use '127.0.0.1' for local testing
    port = 6000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("The connection to the server was refused. Make sure the server is running.")
        return

    print("Connected to the server!")

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f'Response from the server: {data}')
        message = input(" -> ")

    client_socket.close() # Close the connection

if __name__ == '__main__':
    client_program()
