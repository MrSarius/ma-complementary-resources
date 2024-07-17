FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y hping3 iperf3 curl python3 netcat-openbsd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY simple_udp_server.py simple_udp_server.py

CMD ["tail", "-f", "/dev/null"]