def Annonse:
    def __init__(self,annTekst):
        self._annTekst=annTekst
        self._listeBud=[]
    
    def hentTekst(self):
        return self._annTekst
    
    def giBud(self,hvem,belop):
        self._listeBud.append(Bud(hvem,belop))
        
    def antBud(self):
        return len(self._listeBud)
        
    def hoyesteBud(self):
        hoyeste=self._listeBud[0] #Hvis listen er tom vil det skje et exection.
        for i in len(self._listeBud)-1:
            if self._listeBud[i].hentBudStr()>hoyeste.hentBudStr():
                hoyeste=self._listeBud[i]
        return hoyeste
    
    def kraftBud(self,hvem,belop,maxV):
        if belop>self.hoyesteBud():
            self.giBud(hvem,belop)
        elif belop<=self.hoyesteBud():
            if self.hoyesteBud()<maxV:
                self.giBud(hvem,self.hoyesteBud()+1)
