

class Pasient:
    def __init__(self,filnavn):
        self._mutasjoner=[]
        self._lesFil(filnavn)

    def _lesFil(self,filnavn):
        fil=open(filnavn)
        for linje in fil:
            posisjon=int(linje)
            self._mutasjoner.append(posisjon)


    def alleMutasjoner(self):
        #returnerer en liste med mutasjoner.
        return self._mutasjoner

    
