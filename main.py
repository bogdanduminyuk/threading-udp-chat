#UDP Server

from socket import *
from time import ctime
import threading

def server():
    HOST = ''
    PORT = 3000
    BUFSIZE = 1024
    SOCKADDR = (HOST,PORT)
    uServSock = socket(AF_INET,SOCK_DGRAM)
    uServSock.bind(SOCKADDR)
    while True:
        print ('waiting:')
        data,addr = uServSock.recvfrom(BUFSIZE)
        loc_data = data.decode('utf-8') 
        print ('receivedd from: ', addr, ' data: ', loc_data )
        uServSock.sendto(bytearray('[%s] %s' % (ctime(),data), encoding="utf-8"), addr)
    uServSock.close()

#UDP Client
def client():
    HOST = '192.168.1.255'
    PORT = 3000
    BUFSIZE = 1024
    SOCKADDR = (HOST,PORT)
    uCliSock = socket(AF_INET,SOCK_DGRAM)
    uCliSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
            data = input('>')
            print (data)
            data = bytearray(data, encoding='utf-8')
            if not data: break
            uCliSock.sendto(data, SOCKADDR)
            data, addr = uCliSock.recvfrom(BUFSIZE)
            if not data: break
    uCliSock.close()

if __name__ == "__main__":
    serv = threading.Thread(target = server)
    serv.daemon = True
    serv.start()
    
    client()
    
