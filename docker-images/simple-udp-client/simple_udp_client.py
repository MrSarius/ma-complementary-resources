import time
import socket

host = 'localhost'  # Server Service IP address
port = 1234  # Port to connect to


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (host, port)  # Replace with your server's address and port
        while True:
            s.sendto("ping".encode(), server_address)
            data, _ = s.recvfrom(1024)
            print("Client received ping")
            time.sleep(5)


if __name__ == '__main__':
    start_client()
