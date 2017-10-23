class Stasjon:
    def __init__(self,stasjonsnavn):
        self._navn=stasjonsnavn.strip() #Fjerne linjeskift. Burde ikke det heller vaere der fila aapnes.
        self._nabo=[] #Startet som None, men kan ha flere naboer.

    def legg_til_nabo(self,nabo_stasjon):
        self._nabo.append(nabo_stasjon)

    def hent_nabo(self):
        return self._nabo

    def hent_navn(self):
        return self._navn

    def hent_tilfeldig_nabo(self):
        valgt=randint(0,len(self._naboer)-1)
        return self._naboer[valg]
    


def main():
#    trikke_stall=Stasjon("Trikkestallen") #Laget et startpunkt, foer Rikshospitalet.
#    forrige=trikke_stall
#Det over fjernes for aa gjoere det mer generelt.
    for line in open("trikkeplasser.txt"): #Riks-Gaustadalleen-Blindern-osv.
        #["Riksen","Gaustad","Blindern"]:
        denne=Stasjon(line)
        forrige.legg_til_nabo(denne)
        forrige=denne


    stasjonsbok={}
    for linje in open("trase.txt"):
        biter=denne.split()
        frastasjons_navn=biter[0]
        tilstasjons_navn=biter[1]
        if not frastasjons_navn in stasjonsbok:
            stasjonsbok[frastasjons_navn]=Stasjon(frastasjons_navn)         
        frastasjon=stasjonsbok[frastasjons_navn]

        if not tilstasjons_navn in stasjonsbok:
            stasjonsbok[tilstasjons_navn]=Stasjon(tilstasjons_navn)
        tilstasjon=stasjonsbok[tilstasjons_navn]
        
    maal=input("Hvor vil du reise? \n")
    her=trikke_stall
    while her.hent_navn!=maal:
        her = her.hent_nabo()
        print(her.hent_navn())
    print("Du klarte det.")


main()
