#Oppg.1.1. funksjonen adder.

def adder(tall1,tall2):
    summen=tall1+tall2
    return summen

adder(4,3)
adder(2,2)

print("Her er summen av de to variablene: ",adder(4,3))
print("Her er summen av de to variablene: ",adder(2,2))

#Oppg.1.2. telle_bokstav

tekst=input("Skriv inn en tekst: ")
bokstav=input("Hvilken bokstav vil du telle? ")
antall=0

for i in tekst:
    if i==bokstav:
        antall+=1

print(antall)

#Oppg.1.3. tellForekomst, blir veldig likt den over.

def tellForekomst(minTekst=input("Skriv inn en tekst: "), \
                  minBokstav=input("Hvilken bokstav vil du telle? ")):
    antall=0
    for i in minTekst:
        if i==minBokstav:
            antall+=1

    print(antall)

tellForekomst()
