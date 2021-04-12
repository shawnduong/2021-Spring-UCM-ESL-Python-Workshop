# This is a helper I wrote for the workshop. I don't comment too much on this
# since this is a little behind the scenes, but more power to you if you wanna
# take on the challenge and read on!
# - Shawn

def scan(host, port):

	import socket

	try:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.5)

		print(f"[-] Scanning {host}:{port}...", end="\r")
		s.connect((host, port))

		print(f"[+] OPEN PORT DETECTED! {host}:{port}")
		print("The server sent the following message:")
		print(s.recv(1024).decode())
		s.close()

		return True

	except:

		return False

