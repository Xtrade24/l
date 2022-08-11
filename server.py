import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

quit = False
print('[ -- SERVER ONLINE -- ]')

while not quit:
    try:
        data, addr = server.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())

        print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/", end="")
        print(data.decode('utf-8'))

        for client in clients:
            if addr != client:
                server.sendto(data, client)
    except:
        print("\n[ -- SERVER OFFLINE -- ]")
        quit = True

server.close()