from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader=rader
        self._kolonner=kolonner
        self._rutenett=[[Celle() for x in range(self._kolonner)]
                        for y in range(self._rader)]
        self._generasjon=-1 #variabel som holder styr paa generasjonsnummer.
        self.generer()

    def tegnBrett(self):
        for i in range(self._rader):
            rad=""
            for j in range(self._kolonner):
                rad+=self._rutenett[i][j].hentStatusTegn()
            print(rad)

#    def tegnBrett(self):
#        for i in range(self._rader):
#            for j in range(self._kolonner):
#                print(self._rutenett[i][j].hentStatusTegn(),end="")
#            print("")


    def oppdatering(self):
        ny_status_levende=[]
        ny_status_doed=[]
        for i in range(self._rader):
            for j in range(self._kolonner):
                celle_status=self._rutenett[i][j].erLevende()
                naboer=self.finnNabo(i,j)
                antall_levende_naboer=0
                for element in naboer:
                    if element.erLevende()==True:
                        antall_levende_naboer+=1
                    
                if celle_status==True:
                    if antall_levende_naboer<2:
                        ny_status_doed.append(self._rutenett[i][j])
                    elif antall_levende_naboer==2 or antall_levende_naboer==3:
                        pass
                    elif antall_levende_naboer>3:
                        ny_status_doed.append(self._rutenett[i][j])
                    
                elif celle_status==False:
                    if antall_levende_naboer==3:
                        ny_status_levende.append(self._rutenett[i][j])

        for elements in ny_status_levende:
            elements.settLevende()

        for elements in ny_status_doed:
            elements.settDoed()

        self._generasjon+=1


    def finnAntallLevende(self):
        pass

    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand=randint(0,3)
                if rand==3:
                    self._rutenett[i][j].settLevende()
    
    def finnNabo(self,rad,kolonne):
        naboliste=[]
        for i in range(-1,2):
            for j in range (-1,2):
                naboRad=rad+i
                naboKolonne=kolonne+j
                if (naboRad==rad and naboKolonne==kolonne)!=True:
                    if (naboRad<0 or naboKolonne<0 or naboRad>self._rader-1 or naboKolonne>self._kolonner-1)!=True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste

    def generasjon(self):
        return self._generasjon
