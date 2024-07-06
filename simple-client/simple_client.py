import time
import socket

host = '127.0.0.1'  # Server Service IP address
port = 1234  # Port to connect to


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (host, port)
        num = 0
        while True:
            s.sendto(str(num).encode(), server_address)
            data, _ = s.recvfrom(1024)
            print("Client recieved ", data.decode())
            time.sleep(5)
            num = int(data.decode()) + 1


if __name__ == '__main__':
    start_client()
