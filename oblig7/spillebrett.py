from celle import Celle

class Spillebrett:
    def __init__(self,rader,kolonner):
        self._rader=rader
        self._kolonner=kolonner
        self._generasjon=0

        self._rutenett=[[Celle() for x in range(self._kolonner)]
                        for y in range(self._rader)]

    def generasjon(self):
        self._generasjon+=1
        
    def visRutenett(self):
        return self._rutenett
    
