import socket

s = socket.socket()

host_name = socket.gethostname()
host = socket.gethostbyname(host_name)
port = 4202

s.bind((host, port))
s.listen(5)

print('Receiver is listening...')
conn, addr = s.accept()
print('Receiver is connected to', addr)

while True:
    data = conn.recv(1024)
    print('Receiver received', repr(data))
    filename = 'received_file.mp4'
    f = open(filename, 'wb')
    f.write(data)
    f.close()

    conn.send(b'Thank you for sending the file')
    conn.close()