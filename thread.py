import hashlib
from threading import Thread
import time
from itertools import product

class decrypte(Thread):

    
    def __init__(self, charList, shadowLine):
        Thread.__init__(self)
        self.charList = charList
        self.shadowLine = shadowLine

    def run(self):
        for length in range(6, 12):
            i = 0
            to_attempt = product(self.charList, repeat=length);
            start = time.time();
            for attempt in to_attempt:
                i += 1;
                mdp = "".join(attempt);
                if (self.shadowLine[1] == "1"):
                    h = hashlib.md5(mdp.encode("UTF-8").strip()).hexdigest();
                    if (i % 10000000 == 0):
                        middle = time.time();
                        print(self, mdp, self.shadowLine, '%.2gs' % (middle - start))
                    if (h == self.shadowLine[2]):
                        end = time.time();
                        str = "The good passwd is " + mdp.strip() + " for " + self.shadowLine[0].strip() + " " + '%.2gs' % (end - start) + " sec\n";
                        print(str.strip())
                        passFile = open('passFileBrut.txt', 'w')
                        passFile.write(str)
                        passFile.close()


