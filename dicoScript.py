#!/usr/bin/python3
import sys
import time
import hashlib

def parseChar(line):
    line = line.replace('$', ':');
    line = line.replace('::', ':');
    line = line.replace('::', ':');
    line = line.rstrip(" \n");
    return line

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
    passDico(tabPasswd)

def passDico(tabPasswd):
    with open('dico_mini_fr') as dicoFd:
        for line in dicoFd:
            start = time.time();
            for elm in tabPasswd:
                if (elm[1] == "1"):
                    h = hashlib.md5(line.encode("UTF-8").strip()).hexdigest();
                    if (h == elm[2]):
                        end = time.time();
                        str = "The good passwd is " + line.strip() + " for " + elm[0].strip() + " " + '%.2gs' % (end - start) + " sec\n";
                        print(str.strip());
                        with open('passFile.txt', 'w') as passFile:
                            passFile.write(str);

def main(argv):
    if (len(argv) < 1):
        print("Usage : ./dicoScrypt [File]")
        return 2
    with open(argv[0]) as fd:
        makeList(fd)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # Quitte proprement le programme avec les erreurs convenue
