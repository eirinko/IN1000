class Stasjon:
    def __init__(self,stasjonsnavn):
        self._navn=stasjonsnavn.strip() #Fjerne linjeskift. Burde ikke det heller vaere der fila aapnes.
        self._nabo=None

    def legg_til_nabo(self,nabo_stasjon):
        self._nabo=nabo_stasjon

    def hent_nabo(self):
        return self._nabo

    def hent_navn(self):
        return self._navn


def main():
    trikke_stall=Stasjon("Trikkestallen") #Laget et startpunkt, foer Rikshospitalet.
    forrige=trikke_stall
    for line in open("trikkeplasser.txt"): #Riks-Gaustadalleen-Blindern-osv.
        #["Riksen","Gaustad","Blindern"]:
        denne=Stasjon(line)
        forrige.legg_til_nabo(denne)
        forrige=denne

    maal=input("Hvor vil du reise? \n")
    her=trikke_stall
    while her.hent_navn!=maal:
        her = her.hent_nabo()
        print(her.hent_navn())
    print("Du klarte det.")


main()
