import socket

ip = "127.0.0.1"

portlist = [111, 389, 5432, 8086, 8088, 9050]

for port in portlist:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    print(port,":", result)
    sock.close()