#!/bin/sh

scanme_ftp()
{
	while true
	do
		echo "vsftpd-2.3.4" | nc -l -p 21 -q 1
	done
}

# There's an actual real SSH server so this isn't needed for 22.
# SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2

scanme_http()
{
	while true
	do
		echo "nginx/1.14.2" | nc -l -p 80 -q 1
	done
}

scanme_ftp & scanme_http
