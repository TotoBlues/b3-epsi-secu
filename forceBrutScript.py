#!/usr/bin/python3


import argparse
import sys
import getopt
import sys
import hashlib
from thread import decrypte

charList = 'abcdefghijklmnopqrstuvwxyz'
charList += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charList += '0123456789'
charList += '@_#'

# Permet le parsing du fichier (Shadow)
def parseChar(line):
    line = line.replace('$', ':')
    line = line.replace('::', ':')
    line = line.replace('::', ':')
    line = line.rstrip(" \n")
    return line

# Algo qui met dans un tableau les elements pouvant être décrypté
def makeList(fd):
    tabPasswd = []
    
    for line in fd:
        i = 0
        c = 0
        line = parseChar(line)
        for char in line:
            if (char == ':'):
                i += 1
            if (i == 3):
                line = line[:c]
            c += 1
        tabPasswd.append(line.split(':'))
    tabPasswd.pop()
    threadFct(tabPasswd)
            
# Création/départ/arrêt des thread
def threadFct(tabPasswd):
    mThread = []
    i = 0
    
    for elm in tabPasswd:
        mThread.append(decrypte(charList, elm, str(i)));
        i += 1
    for elm in mThread:
        elm.start();
    for elm in mThread:
        elm.join();


def main(argv):
    if (len(argv) < 1):
        print("Usage : ./dicoScrypt [File]")
        return 2
    with open(argv[0]) as fd:
        makeList(fd)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # Quitte proprement le programme avec les erreurs convenue
