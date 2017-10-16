#!/usr/bin/python3

fd = open('shadow');
tabPasswd = [];

for line in fd:
    line = line.replace('$', ':');
    line = line.replace('::', ':');
    line = line.replace('::', ':');
    line = line.rstrip(" \n");
    line = line[];
    tabPasswd.append(line.split(':'));

#for elm in tabPasswd: 
#    print(elm);
fd.close();
