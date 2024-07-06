import socket
import time

# Server settings
host = '0.0.0.0'  # Server IP address
port = 1234  # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        while True:
            data, addr = s.recvfrom(1024)
            print("Server recieved ", data.decode())
            time.sleep(5)
            num = int(data.decode()) + 1
            s.sendto(str(num).encode(), addr)


if __name__ == '__main__':
    start_server()