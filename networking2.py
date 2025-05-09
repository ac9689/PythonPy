import socket

# 1. Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server
client_socket.connect(('0.0.0.0', 8080))

# 3. Send a message
client_socket.send("Hi Server!".encode())

# 4. Receive server response
response = client_socket.recv(1024).decode()
print("Server says:", response)

# 5. Close connection
client_socket.close()
