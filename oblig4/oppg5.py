#Oppg.5.1. Oppgavetekst.
# Du skal lage et system for aa holde styr paa venners bursdager.
# a. Lag to tomme lister - en som etter hvert skal inneholde navn og den andre for fodselsdato.
# b. Lag et system der du faar legge inn baade navn og dato for en venns fodselsdag: legg inn en person.
# c. Lag listen "bursdager, som inneholder begge deler.
# d. Bruk dette for aa legge inn fem fodselsdager fra venner og familie.

#Oppg.5.1.a.
navn=[]
dag=[]
mnd=[]
aar=[]
fodselsdato=[dag, mnd, aar]


#Oppg.5.1.b.
def legg_til_bursdag(antall):
    for i in range(antall):
        navn.append(input("Hva er navnet paa personen? "))
        dag.append(input("Hva er fodselsdagen? Forst dag: "))
        mnd.append(input("Hva er fodselsdagen? Deretter maaned: "))
        aar.append(input("Hva er fodselsdagen? Til slutt fodselsaaret: "))
        

#Burde vaere en sjekk paa om fodselsdag er lagt inn riktig.

legg_til_bursdag(1)

#Oppg.5.1.c.
bursdager=[navn,fodselsdato]

print(bursdager)

#Oppg.5.1.d.
legg_til_bursdag(5)
