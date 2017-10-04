#Oppg.4.1. Lage klassen Hund.
class Hund:
    def __init__(self,alder,vekt,metthet):
        self._alder=alder
        self._vekt=vekt
        self._metthet=10

#Oppg.4.2. Returnerer alder og vekt for hunden.
    def returnerAlder(self):
        return self._alder
    
    def returnerVekt(self):
        return self._vekt

#Oppg.4.3. Endrer metthet og potensielt vekt naar hunden bruker spring().
    def spring(self):
        self._metthet-=1
        if self._metthet<5:
            self._vekt-=1

#Oppg.4.4. Endrer metthet og potensielt vekt når hunden bruker spis().
    def spis(self):
        self._metthet+=1
        if self._metthet>7:
            self._vekt+=1
