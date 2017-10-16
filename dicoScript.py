#!/usr/bin/python3

fd = open('shadow');
dicoFd = open('dico_mini_fr');
tabPasswd = [];

for line in fd:
    i = 0;
    c = 0;
    line = line.replace('$', ':');
    line = line.replace('::', ':');
    line = line.replace('::', ':');
    line = line.rstrip(" \n");
    print(line);
    for char in line:
        if (char == ':'):
            i += 1;
        if (i == 3):
            line = line[:c];
        c += 1;
    tabPasswd.append(line.split(':'));

for elm in tabPasswd: 
    print(elm);

dicoFd.close();
fd.close();
