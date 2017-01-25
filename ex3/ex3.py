# python code
#from threading import Lock

import socket
from threading import Thread
import time

port=30000
port2=20015


serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind(('',port))

for i in range(2):
    message, server_address =serverSocket.recvfrom(1024)
    print(message, server_address)
serverSocket.close()

message_to_send="Here we are"


def listen(port_to_listen):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSocket.bind(('',port_to_listen))
    serverSocket.settimeout(1.)
    try:
        for i in range(3):
            message, server_address =serverSocket.recvfrom(len(message_to_send)+1+len('You said:'))
            print(message, server_address)

        serverSocket.close()
        return 0
    except:
        print('Time out!')        
        pass
        

def client(port_to_send):
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #clientSocket.bind(('129.241.187.43',port_to_send))
    clientSocket.sendto("Here we are", ("129.241.187.43",port_to_send))
    clientSocket.close()



############### Test UDP send   ######################

Thread_0 = Thread(target = listen,args=(port2,))
Thread_0.start()

#time.sleep(2)

Thread_1 = Thread(target = client,args=(port2,))
Thread_1.start()

  
Thread_0.join()
Thread_1.join()


