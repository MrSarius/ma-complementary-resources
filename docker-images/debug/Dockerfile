FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y hping3 iperf3 netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["tail", "-f", "/dev/null"]