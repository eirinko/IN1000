#Oppg5 Maalene skal over i en ordbok. Lager ogsaa hovedprogram der alt skal kalles.
def fraFiltilOrdbok(fil):
    ordbok={}
    for linje in open(fil,"r"):
        maal=linje.split(" ")
        navn=maal[0]
        verdi=float(maal[1])
        ordbok[navn]=verdi
    return ordbok

def tommerTilCm(antallTommer):
    assert antallTommer>0
    return antallTommer*2.54

def tommertilCmListe(liste):
    for i in liste:
        Cm=tommerTilCm(i)
        print(Cm)

def hovedprogram():  
    maalboka=fraFiltilOrdbok("skreddermaal.txt")
    print(maalboka)
    maal_liste=[4,3.2,10,32] #Vil egentlig hente verdiene fra maalboka, men hadde ikke tid.
    tommertilCmListe(maal_liste)

hovedprogram()
