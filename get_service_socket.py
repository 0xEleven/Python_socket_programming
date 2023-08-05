import socket

def find_service_name():
    for port in [21,22,23,25,80]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, "tcp")))
        print("Port: %s => service name: %s"%(53, socket.getservbyport(53, "udp")))
if __name__ == "__main__":
    find_service_name()
