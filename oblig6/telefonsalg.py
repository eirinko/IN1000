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
    print("Maanedens salgsperson er ", person, ", med ", salgstall, " salg.")

#Oppg.1.3. En funksjon som regner ut totalsalg den maanden.
def totalAntallSalg(ordbok):
    totalt=0
    for navn in ordbok:
        totalt=totalt+ordbok[navn]
    return totalt

#Oppg.1.4. En funksjon som gir gjennomsnittlig salg per person.
#Bruker resultatet fra totaltAntallSalg og deler paa antallet i lista.
def gjennomsnittSalg(ordbok):
    return totalAntallSalg(ordbok)/len(ordbok)

#Oppg.1.5. Hovedprogrammet der funksjonene over kalles paa og resultat skrives ut som i oppgaven.
def hovedprogram():
    OrdbokSalgstall=innlesing("salgsstatistikk.txt")
    maanedensSalgsperson(OrdbokSalgstall)
    print("Aktive selgere denne maaneden: ", len(OrdbokSalgstall))
    print("Totalt antall salg: ",totalAntallSalg(OrdbokSalgstall))
    print("Gjennomsnittlig antall salg per salgsperson: ", gjennomsnittSalg(OrdbokSalgstall))

hovedprogram()
