def Annonse:
    def __init__(self,annTekst):
        self._annTekst=annTekst
        self._listeBud=[]
        antLaveBud=0
    
    def hentTekst(self):
        return self._annTekst
    
    def giBud(self,hvem,belop):
        self._listeBud.append(Bud(hvem,belop))
        hoyeste=self.hoyesteBud()
        if belop<hoyeste.hentBudStr():     #Oppg.4g)
            antLaveBud+=1
        
    def antBud(self):
        return len(self._listeBud)
        
    def hoyesteBud(self):
        hoyeste=0
        for i in len(self._listeBud)-1:
            if self._listeBud[i].hentBudStr()>hoyeste:
                hoyeste=self._listeBud[i].hentBudStr()
        return hoyeste
        
    def antLaveBud(self): #Oppg.4g)
        return antLaveBud
