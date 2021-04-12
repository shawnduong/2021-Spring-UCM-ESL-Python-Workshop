# Workshop 3: Creating a Port Scanner

Let's suppose that you work for a cybersecurity firm, and a client has recently hired your company to audit the security of one of their servers. One of the things on your checklist is to scan the server to find out what services are running on it in addition to the versions of said services. You could manually try connecting to each port on the target, but instead, you decide to make a tool to do this using Python.

**Objective:** use Python to write a port scanner that will discover services on the target server. Find out which services are vulnerable on the target server.

**Disclaimer:** the IP address of the target will be given through the Zoom call during the workshop. This is a safe target server set up by the organizers of the workshop for attendees to scan. **You have legal permission to scan this target.** This workshop provides a controlled lab environment. In the real world, please do not scan targets you do not have written permission for.

## Scope

You may scan the target whose IP address was given during the Zoom call. You can scan all the ports on this target, but there's no point scanning beyond TCP port 100 as all open services on the target machine have a port less than 100.

## Step-by-Step Instructions
