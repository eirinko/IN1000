from annonse import Annonse

class Kategori:
    def __init__(self,katNavn):
        self._katNavn=katNavn
        self._katListe=[]
        
    def nyAnnonse(self,annTekst):
        a=Annonse(annTekst)
        self._katListe.append(a)
        return a
        
    def hentAnnonser(self):
        return self._katListe
