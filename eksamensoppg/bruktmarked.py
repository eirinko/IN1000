class Bruktmarked:
    def __init__(self):
        oversiktKat={}
        
    def nyKategori(self,katNavn):
        if katNavn in oversiktKat:
            return None
        else:
            oversiktKat[katNavn]=Kategori(katNavn)
            return oversiktKat[katNavn]
        
        
    def finnKategori(self,katNavn):
        if katNavn in oversiktKat:
            return oversiktKat[katNavn]
        else:
            return None
