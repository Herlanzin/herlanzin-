import socket

host = '127.0.0.1'
port = 5050
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print ('agurdando uma conexeçaó')
conn, ender = s.accept()
print ('conectado em ', ender)
while True:
	data = conn.recv(1024)
	if not data:
		print ('fechando a conexaõ')
		conn.close()
		break
	conn.sendall(data)