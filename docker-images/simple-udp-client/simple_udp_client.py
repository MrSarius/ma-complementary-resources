import time
import socket

host = '10.30.0.1'  # Server Service IP address
port = 1234  # Port to connect to


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = ('localhost', 12345)  # Replace with your server's address and port
        num = 0
        while True:
            # Send a message to the server
            s.sendto(str(num).encode(), server_address)

            # Wait for a response from the server
            data, _ = s.recvfrom(1024)
            print("Client received:", data.decode())

            # Increment the counter and prepare the next message
            num += 1

            # Send a reply back to the server
            s.sendto(f"Reply to {data.decode()}".encode(), server_address)
            time.sleep(5)


if __name__ == '__main__':
    start_client()
