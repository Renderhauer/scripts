from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import select
import threading
import time
import platform


print('='*30)
print('Chimera chat v0.9 by Renderhauer')
print('\nFor now works only in local network!')
print('\nChimera use straight connection to your opponent,')
print("so you have to know your friend's IP and port,")
print('where he is going to listen for you. The other side,')
print('he must know your IP and port, which you opened.')
print('\nKnown issue - recieving message while typing')
print('will break your message')
print('='*30)


def intro():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    print('Your local IP: ' + a)
    s.close()
    b = input('Enter your port: ')
    c = input('Enter target ip: ')
    d = input('Enter target port: ')
    return a, b, c, d


def recieve_message(timed):
    for i in range(timed):
        try:
            (data, addr) = mySocket.recvfrom(SIZE)
            print('\r>> [IN]: ' + data.decode("utf-8") + ' ' + '\n< [OUT]: ', end='')
        except:
            pass


def send_message(outputs):
    for ii in range(outputs):
        try:
            myMessage = input('< [OUT]: ')
            mySocket.sendto(myMessage.encode('utf-8'), (SERVER_IP, HIS_PORT_NUMBER))
        except:
            pass

timed = 43200
outputs = 10000
SIZE = 1024
my_pc_name = platform.node()

a, b, c, d = intro()
hostName = gethostbyname(a)
MY_PORT_NUMBER = int(b)
HIS_PORT_NUMBER = int(d)
SERVER_IP = c
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, MY_PORT_NUMBER))
print('Connecting...')
time.sleep(1)

mySocket.sendto(('>>[SYS] '+ my_pc_name + ' connected to you!').encode('utf-8'), (SERVER_IP, HIS_PORT_NUMBER))
(data, addr) = mySocket.recvfrom(SIZE)
print(data.decode("utf-8"))

mySocket.settimeout(1)

try:
	mySocket.sendto(('>>[SYS] '+ my_pc_name + ' connected to you!').encode('utf-8'), (SERVER_IP, HIS_PORT_NUMBER))
	(data, addr) = mySocket.recvfrom(SIZE)
	print(data.decode("utf-8"))
except:
	pass


print('='*30)
recieve = threading.Thread(target=recieve_message, args=(timed,))
send = threading.Thread(target=send_message, args=(outputs,))
recieve.start()
send.start()