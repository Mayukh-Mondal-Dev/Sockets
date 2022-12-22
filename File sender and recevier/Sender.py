import socket
import glob

s = socket.socket()

host = str(input("Enter the host name: "))


s.connect((host, 4202))


for file in glob.glob(r"C:\Github_repo\Sockets\File sender and recevier\test.mp4"):
    with open(file, "rb") as f:
        s.sendall(f.read())

s.close()