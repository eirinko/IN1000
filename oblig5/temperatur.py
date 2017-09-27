#Oppg.2.1.Lager en liste aarstemp med temperaturer for hver mnd.
#Har ikke gjort om fra str til float eller int.
aarstemp=[]
for linje in open("temperatur.txt"):
    verdi=linje.strip("\n")
    aarstemp.append(verdi)
#Deretter skrives den ut.
print(aarstemp)

#Oppg.2.2. en funksjon skal ta imot en liste og lage gjennomsnitt.
#Hvis denne skal vaere generell trenger vi en variabel som telle iterasjoner.
def gj_snitt(liste):
    antall=0
    summen=0
    for verdi in liste:
        verdi=float(verdi)
        antall+=1
        summen+=verdi
    return summen/antall

gj_snitt_aarstemp=gj_snitt(aarstemp)
print(gj_snitt_aarstemp)
