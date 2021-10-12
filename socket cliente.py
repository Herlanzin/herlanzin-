import socket
host = '127.0.0.1'
port = 5050
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(str.encode('bom dia'))
data = s.recv(1024)
print('mensagem', data.decode())
