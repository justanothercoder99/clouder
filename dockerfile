FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev && \
    apt-get install -y curl && \
    apt-get clean

# RUN pip3 install dependencies.txt # Not required for now
RUN mkdir -p /home/data/output
WORKDIR /home/data

COPY *.py /home/data
COPY IF-1.txt /home/data
COPY AlwaysRememberUsThisWay-1.txt /home/data

CMD ["python3", "main.py"]