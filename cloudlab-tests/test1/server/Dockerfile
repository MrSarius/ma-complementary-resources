FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y iperf3 netcat&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY run.sh run.sh

RUN chmod +x run.sh

CMD ["bash", "run.sh"]