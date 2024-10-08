import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on UDP port {UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    sock.sendto(b"ACK", addr)