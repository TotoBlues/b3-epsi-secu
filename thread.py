import hashlib
from threading import Thread
import time
from itertools import product

class decrypte(Thread):

    # Reféfinis la valeur de l'initialisation d'un thread
    def __init__(self, charList, shadowLine):
        Thread.__init__(self)
        self.charList = charList
        self.shadowLine = shadowLine

    # Fonction appelée après avoir trouvé le bon mdp
    def findPass(self, mdp):
        end = time.time();
        str = "The good passwd is " + mdp.strip() + " for " + self.shadowLine[0].strip() + " " + '%.2gs' % (end - start) + " sec\n";
        print(str.strip())
        passFile = open('passFileBrut.txt', 'a')
        passFile.write(str)
        passFile.close()

    # La boucle de calcule
    def run(self):
        for length in range(6, 12):
            to_attempt = product(self.charList, repeat=length);
            start = time.time();
            for attempt in to_attempt:
                mdp = "".join(attempt);
                if (self.shadowLine[1] == "1"):
                    h = hashlib.md5(mdp.encode("UTF-8").strip()).hexdigest();
                    if (h == self.shadowLine[2]):
                        findPass(self, mdp);
                if (self.shadowLine[1] == "5"):
                    h = hashlib.sha256(mdp.encode("UTF-8").strip()).hexdigest();
                    if (h == self.shadowLine[2]):
                        findPass(self, mdp);    
                if (self.shadowLine[1] == "6"):
                    h = hashlib.sha512(mdp.encode("UTF-8").strip()).hexdigest();
                    if (h == self.shadowLine[2]):
                        findPass(self, mdp);

