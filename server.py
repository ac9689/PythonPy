import socket
s=socket.socket()
print('socket Created ')

s.bind(('127.0.0.1', 1234))
s.listen(3)
print('waiting for connections')

while True:
    c, addr = s.accept()
    name=c.recv(1024).decode()
    print("connected with", addr, name)
    
    c.send(bytes('Welcome to India', 'utf-8'))
    
    c.close()