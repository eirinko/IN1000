#Oppg.4.1. lager en tom liste og brukeren skal fylle denne med fem reisemaal.

steder=[]

def legge_til(lista,spm):
    for i in range(5):
        lista.append(input(spm))

#def legge_til_v2(spm):
#    lista = []
#    for i in range(5):
#        lista.append(input(spm))
#    return lista

legge_til(steder, "Hvor vil du dra? ")

#Oppg.4.2.

klesplagg=[]
avreisedatoer=[]

legge_til(klesplagg,"Skriv inn klesplagg for reisen: ")
legge_til(avreisedatoer, "Skriv inn dato for avreise: ")

#Oppg.4.3.

reiseplan=[steder, klesplagg, avreisedatoer]

print(reiseplan)

#Oppg.4.4. For each der de tre listene skrives ut med hvert sitt innhold.

for i in reiseplan:
    print(i)

#Oppg.4.5.a. 
i1=[0,1,2]

#Oppg.4.5.b.
i2=[0,1,2,3,4]

#Oppg.4.5.c.

def gyldig_input():
    valgt_liste=int(input("Skriv hvilken liste du vil inn i fra reiseplanen (0,1,2): "))
    valgt_plass=int(input("Skriv hvilken plass du vil ha i listen (0,1,2,3,4): "))
    if (valgt_liste in i1) and (valgt_plass in i2):
        print(reiseplan[valgt_liste][valgt_plass])
    else:
        print("Ugyldig input!")

gyldig_input()
