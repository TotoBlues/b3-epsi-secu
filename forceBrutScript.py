#!/usr/bin/python3

import sys
import hashlib
from thread import decrypte


fd = open('shadow');
tabPasswd = [];
mThread = []

charList = 'abcdefghijklmnopqrstuvwxyz';
charList += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
charList += '0123456789';
charList += '@_#';

complete_list = [];

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

for elm in tabPasswd:
    if (elm[1] == "1"):
        mThread.append(decrypte(charList, elm));
    
for elm in mThread:
    elm.start();
for elm in mThread:
    elm.join();

'''
for length in range(6, 12):
    to_attempt = product(charList, repeat=length);
    for elm in tabPasswd:
        start = time.time();
        for attempt in to_attempt:
            mdp = "".join(attempt);
            if (elm[1] == "1"):
                h = hashlib.md5(mdp.encode("UTF-8").strip()).hexdigest();
                if (h == elm[2]):
                    end = time.time();
                    print(mdp);
                    str = "The good passwd is " + mdp.strip() + " for " + elm[0].strip() + " " + '%.2gs' % (end - start) + " sec\n";
                    print(str.strip());
                    passFile.write(str);
'''
fd.close();
