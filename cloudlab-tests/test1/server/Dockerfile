FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y iperf3 python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY run.sh run.sh
COPY simple_udp_server.py simple_udp_server.py

RUN chmod +x run.sh

CMD ["bash", "run.sh"]