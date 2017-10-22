import hashlib
from threading import Thread, RLock
import time
import pickle
from itertools import product

class decrypte(Thread):

    # Reféfinis la valeur de l'initialisation d'un thread
    def __init__(self, charList, shadowLine, nom):
        Thread.__init__(self)
        self.nom = nom
        self.charList = charList
        self.shadowLine = shadowLine
       
    # Fonction appelée après avoir trouvé le bon mdp
    def findPass(self, mdp, start):
        end = time.time();
        str =  "The good passwd is " + mdp.strip() + " for " + self.shadowLine[0].strip() + " " + '%.2gs' % (end - start) + "\n";
        print(self, str.strip())
        passFile = open('passFileBrut.txt', 'a')
        passFile.write(str)
        passFile.close()
        return True

    # La boucle de calcule
    def run(self):
        find = False
        passe = False
        
        for length in range(6, 13):
            if (find == False):
                to_attempt = product(self.charList, repeat=length);
                start = time.time();
                for attempt in to_attempt:
                    mdp = "".join(attempt);
                    now = time.time()
                    if ((round(now) - round(start)) % 600 == 0 and passe == False):
                        with RLock():
                            recovery = open('recovery', 'a')
                            recovery.write('Thread is ' + self.nom + ' mdp is ' + mdp + ' time is : ' + str((now - start)) + '\n')
                            recovery.close();
                            passe = True
                    if (self.shadowLine[1] == "1"):
                        h = hashlib.md5(mdp.encode("UTF-8").strip()).hexdigest();
                        if (h == self.shadowLine[2]):
                            find = self.findPass(mdp, start);
                    if (self.shadowLine[1] == "5"):
                        h = hashlib.sha256(mdp.encode("UTF-8").strip()).hexdigest();
                        if (h == self.shadowLine[2]):
                            find = self.findPass(mdp, start);    
                    if (self.shadowLine[1] == "6"):
                        h = hashlib.sha512(mdp.encode("UTF-8").strip()).hexdigest();
                        if (h == self.shadowLine[2]):
                            find = self.findPass(mdp, start);
                            print(self, mdp);
                    if (round(now) - round(start) % 10 == 0):
                        passe = False
                    if (find == True):
                        break;

