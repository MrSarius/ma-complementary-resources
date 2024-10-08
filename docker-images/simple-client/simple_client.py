# import time
# import socket
#
# host = '10.30.0.1'  # Server Service IP address
# port = 1234  # Port to connect to
#
#
# def start_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         server_address = (host, port)
#         s.settimeout(1.0)
#         num = 0
#         while True:
#             s.sendto(str(num).encode(), server_address)
#             try:
#                 data, _ = s.recvfrom(1024)
#                 print("Client recieved ", data.decode())
#                 num += 1
#             except socket.timeout:
#                 print("Client timeout")
#
#             time.sleep(5)
#
#
# if __name__ == '__main__':
#     start_client()

import socket
import time

host = '10.30.0.1'  # Server Service IP address
port = 1234  # Port to connect to

time.sleep(5)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(str(0).encode())
    while True:
        data = s.recv(1024)
        if not data:
            break
        msg = data.decode()
        print('Client received:', msg)
        time.sleep(5)
        s.sendall(str(int(msg) + 1).encode())