FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python3.9 -y
RUN apt-get install python3-pip -y
RUN pip3 install pandas

WORKDIR /tada/casestudy
COPY . .
CMD ["python3", "./main.py"]
