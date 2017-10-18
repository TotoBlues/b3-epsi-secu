#!/usr/bin/python3

import hashlib
import time
from itertools import product

fd = open('shadow');
tabPasswd = [];

#abcdefghijklmnopqrstuvwxyz
charList = 'brazil';
#charList += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
#charList += '0123456789';
#charList += '@_#';

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

i = 0;

for length in range(6, 7):
    to_attempt = product(charList, repeat=length);
    for elm in tabPasswd:
        for attempt in to_attempt:
            i += 1;
            mdp = ''.join(attempt);
            if (elm[1] == "1"):
                h = hashlib.md5(mdp.encode("UTF-8").strip()).hexdigest();
                print(h, elm[2], mdp);
                if (h == elm[2]):
                    print(mdp);

fd.close();
