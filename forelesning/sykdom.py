#Representasjon av klassen.
#Maa ta vare paa posisjon i klassen.
#self._posisjonser: list
#Maa kunne lagre navn paa sykdommen.
#self._navn: str

class Sykdom:
    def __init__(self,navn):
        self._navn=navn
        self._posisjoner=[]

    def leggTilPosisjon(self,posisjon):
        self._posisjoner.append(posisjon)
        print(self._posisjoner)

    def erAssosiert(self,posisjon):
        return posisjon in self._posisjoner

    #def hentAntallTreff(self): for aa telle antall overlapp med en sykdom.
    #gjoer endring i sykdomsKatalog ogsaa.
