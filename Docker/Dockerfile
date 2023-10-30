FROM ubuntu:20.04

# We need this to avoid the interactive prompts during the installs
ENV DEBIAN_FRONTEND=noninteractive 

RUN yes | unminimize \ 
  && apt-get install -y man-db build-essential gdb

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "gcc-multilib"]

WORKDIR /root

RUN mkdir /root/host

ENTRYPOINT ["bash"]

# docker build -t ubuntu:20.04 .

# docker run -h Jair-Meza -v C:\Users\MSI\Desktop\CS-2011:/root/host --rm -it ubuntu:20.04
