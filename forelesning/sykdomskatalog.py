from sykdom import Sykdom

class SykdomsKatalog:
    def __init__(self,filnavn):
        self._sykdommer={}
        self._lesFil(filnavn)
        print(self._sykdommer)


    def _lesFil(self,filnavn): #Hver linje har tall,navn.
        fil=open(filnavn)
        for line in fil:
            biter=line.split(",")
            posisjon=int(biter[0])
            sykdomsnavn=biter[1].strip()
            if sykdomsnavn in self._sykdommer:
                sykdom=self._sykdommer[sykdomsnavn]
            else:
                sykdom=Sykdom(sykdomsnavn)
                self._sykdommer[sykdomsnavn]=sykdom
            sykdom.leggTilPosisjon(posisjon)

    def sjekkMutasjon(self,posisjon): #samme som erAssosiert
        for sykdomnavn in self._sykdommer:
            sykdom=self._sykdommer[sykdomsnavn]
            if sykdom.erAssosiert(posisjon):
                print("Posisjon",posisjon,"er assosiert med",sykdomsnavn)
                
