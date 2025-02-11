# Use the official FRR image as our base.
FROM frrouting/frr:latest

RUN apk update && apk add openssh


RUN echo "root:ffr" | chpasswd


RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

COPY start.sh /start.sh
RUN chmod +x /start.sh

# Use our startup script as the container’s entrypoint.
ENTRYPOINT ["/start.sh"]
