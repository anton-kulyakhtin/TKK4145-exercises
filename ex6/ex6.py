#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:13:35 2017

@author: anton
"""

import subprocess
import socket
import time


Use_port=20015


def broadcast_and_print(port,i_start):
    
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    host_name = socket.gethostname() # Get local machine name
    my_address = socket.gethostbyname(host_name)
    #clientSocket.sendto("Here we are", ("129.241.187.43",port))
    
    for i in range(i_start,1000):
        time.sleep(1)
        msg="Number is %d"%i
        clientSocket.sendto(msg.encode(), (my_address,port))
        print("Number is %d"%i)
    clientSocket.close()

def back_up_process(port):
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSocket.bind(('',port))
    serverSocket.settimeout(2.)
    message_receive_size=100
    local_i=0
    try:
        while(1):
            message, server_address =serverSocket.recvfrom(message_receive_size)
            #print(message, server_address)
            print('received:', message.decode(), server_address) # python 3
            local_i=int(message.decode().split()[2])            

        serverSocket.close()
        return 0
    except socket.timeout:
        serverSocket.close()
        print('did not hear the primary for 5 seconds!')        
        print('Im primary!')
        pass
    except:
        serverSocket.close()
        raise
    subprocess.Popen(['gnome-terminal','-x', 'python','ex6.py'])
    broadcast_and_print(port,local_i+1)    

        
back_up_process(Use_port)
    
