#!/usr/bin/python3

fd = open('shadow');
tabPasswd = [];

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

for current in range(5,12):
    a = [i for i in charList];
    for y in range(current):
        a = [x + i for i in charList for x in a];
    complete_list = complete_list + a;
    print(complete_list);
fd.close();
