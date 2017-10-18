#!/usr/bin/python3

import time
import hashlib

fd = open('shadow');
passFile = open('passFile.txt', 'w');
dicoFd = open('dico_mini_fr');
tabPasswd = [];

def parseChar(line):
    line = line.replace('$', ':');
    line = line.replace('::', ':');
    line = line.replace('::', ':');
    line = line.rstrip(" \n");
    return line

for line in fd:
    i = 0;
    c = 0;
    line = parseChar(line);
    for char in line:
        if (char == ':'):
            i += 1;
        if (i == 3):
            line = line[:c];
        c += 1;
    tabPasswd.append(line.split(':'));
tabPasswd.pop();

for line in dicoFd:
    start = time.time();
    for elm in tabPasswd:
        if (elm[1] == "1"):
            h = hashlib.md5(line.encode("UTF-8").strip()).hexdigest();
            if (h == elm[2]):
                end = time.time();
                str = "The good passwd is " + line.strip() + " for " + elm[0].strip() + " " + '%.2gs' % (end - start) + " sec\n";
                print(str.strip());
                passFile.write(str);

dicoFd.close();
passFile.close();
fd.close();
