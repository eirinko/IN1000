class Bruktmarked:
    def __init__(self):
        self._oversiktKat={}
        
    def nyKategori(self,katNavn):
        if katNavn in self._oversiktKat:
            return None
        else:
            self._oversiktKat[katNavn]=Kategori(katNavn)
            return self._oversiktKat[katNavn]
        
        
    def finnKategori(self,katNavn):
        if katNavn in self._oversiktKat:
            return self._oversiktKat[katNavn]
        else:
            return None
