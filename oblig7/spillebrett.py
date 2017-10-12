from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader=rader
        self._kolonner=kolonner
        self._rutenett=[[Celle() for x in range(self._kolonner)]
                        for y in range(self._rader)]
        self._generasjon=0 #variabel som holder styr paa generasjonsnummer.
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
        pass

    def finnAntallLevende(self):
        pass

    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand=randint(0,3)
                if rand==3:
                    self._rutenett[i][j].settLevende()
    
    def finnNabo(self,x,y):
        naboliste=[]
        for i in range(-1,2):
            for j in range (-1,2):
                naboX=x+i
                naboY=y+j
                if (naboX==x and naboY==y)!=True:
                    if (naboX<0 or naboY<0 or naboX>self._kolonner-1 or naboY>self._rader-1)!=True:
                        naboliste.append(self._rutenett[naboY][naboX])
        return naboliste

    def generasjon(self):
        self._generasjon+=1


        
