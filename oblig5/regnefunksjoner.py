#Oppg.1.1. Lager en funksjon som heter addisjon for aa legge sammen to tall.

def addisjon(a,b):
    return a+b

pluss=addisjon(2,3)
print(pluss)

#Oppg.1.2. Lager funksjoner for subtraksjon, divisjon.
def subtraksjon(a,b):
    return a-b

def divisjon(a,b):
    return a/b

#Funksjonene skal sjekkes ved hjelp av assert, minst tre assert-uttrykk.
#Forst for subtraksjon:
assert subtraksjon(10,8)==2
assert subtraksjon(-10,-2)==-8
assert subtraksjon(-2,2)==-4

#Deretter for divisjon:
assert divisjon(10,5)==2
assert divisjon(-10,-5)==2
assert divisjon(-10,5)==-2

#Faar ingen assertion-errors med dette. Gaar derfor videre til neste oppg.
#Oppg.1.3.
def tommerTilCm(antallTommer):
    assert antallTommer>0
    return antallTommer*2.54

assert tommerTilCm(1)==2.54
assert tommerTilCm(2)==5.08
#Hadde lyst til aa sjekke at det blir asserion-error naar antallTommer=-1, men faar ikke til.

#Oppg.1.4.a.
def skrivBeregninger():
    x=float(input("Skriv inn et tall: "))
    y=float(input("Skriv inn et tall til: "))
    print("Resultat av addisjon: ", addisjon(x,y))
    print("Resultat av subtraksjon: ", subtraksjon(x,y))
    print("Resultat av divisjon: ", divisjon(x,y))
#Oppg.1.4.b.
    z=float(input("Konvertering fra tommer til cm: \n Skriv inn et tall: "))
    print("Resultat: ", tommerTilCm(z))

skrivBeregninger()
