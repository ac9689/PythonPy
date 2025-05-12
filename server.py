import socket

# 1. Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to localhost and port 12345
server_socket.bind(('192.168.29.17', 12345))

# 3. Listen for connections
server_socket.listen(1)
print("Server is listening...")

# 4. Accept a client
client_socket, client_address = server_socket.accept()
print(f"Connected with {client_address}")

# 5. Receive data
data = client_socket.recv(1024).decode()
print("Received from client:", data)

# 6. Send response
client_socket.send("Hello from server!".encode())

# 7. Close connections
client_socket.close()
server_socket.close()
