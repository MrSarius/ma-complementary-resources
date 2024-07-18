FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y hping3 iperf3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*