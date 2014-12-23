import socket
from random import randrange
import threading

print """RISC
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Random IP Scan                       | karaayaz_"""
print ""

def GenerateIP():
   ip0 = randrange(0,256)
   ip1 = randrange(0,256)
   ip2 = randrange(0,256)
   ip3 = randrange(0,256)
   return str(ip0)+"."+str(ip1)+"."+str(ip2)+"."+str(ip3)

class scan(threading.Thread):
   def run(self):
      while 1:
         try:
            target = GenerateIP()
            s=socket.socket()
            s.connect((target, 80))
            print "--> "+target
            s.close()
         except:
            pass

for i in xrange(150):
   t = scan()
   t.start()
