#!/bin/bash
ssh-keygen -A

/usr/sbin/sshd &

exec /usr/lib/frr/docker-start "$@"
