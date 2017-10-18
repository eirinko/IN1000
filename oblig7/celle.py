#Lager klassen celle.
class Celle:
    def __init__(self):
        self.settDoed()
        #Bruker Celle-klassens egen metode for aa sette foerste status til doed=False.

    def settDoed(self):
        self._status=False
        #I stedet for aa skrive "doed" valgte jeg aa bruke False som tegn paa
        #doed og True  som tegn paa levende. Det forenkler en del av koden.

    def settLevende(self):
        self._status=True

    def erLevende(self):
        return self._status
        #Returnerer self._status, som enten er True eller False.

    def hentStatusTegn(self):
        if self._status==True:
            return "O"
        else:
            return "."
