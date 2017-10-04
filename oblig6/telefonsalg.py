#Oppg.1.1. Innleding av data fra fil. Returnerer en ordbok.
def innlesing(filnavn):
    ordbok={}
    for linje in open(filnavn,"r"):
        liste=linje.split(" ")
        navn=liste[0]
        tall=int(liste[1])
        ordbok[navn]=tall
    return ordbok

#Oppg.1.2. Definerer en funksjon som evaluerer en ordbok.
#Skriver ut navn og antall salg for personen som har solgt mest.
def maanedensSalgsperson(ordbok):
    person=""
    salgstall=0
    for navn in ordbok:
        if ordbok[navn]>salgstall:
            salgstall=ordbok[navn]
            person=navn
    print("Dette er maanedens salgsperson: ", person)
    print("Dette er maanedens beste salgstall: ", salgstall)

#Oppg.1.3. En funksjon som regner ut totalsalg den maanden.
def totalAntallSalg(ordbok):
    totalt=0
    for navn in ordbok:
        totalt=totalt+ordbok[navn]
    return totalt

#Oppg.1.4. En funksjon som gir gjennomsnittlig salg per person.
#Bruker resultatet fra totaltAntallSalg og deler paa antallet i lista.
def gjennomsnittSalg(tot,ordbok):
    


def hovedprogram():
    salgstall=innlesing("salgsstatistikk.txt")
    maanedensSalgsperson(salgstall)

hovedprogram()
