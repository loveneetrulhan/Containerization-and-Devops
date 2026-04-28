FROM ubuntu

RUN apt update && apt install -y openssh-server python3 sudo

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
