#Oppg.4.1.
#Nei, i print inne i if-setningen blir en integer og en string lagt sammen.
# Det fører til en Error og ingenting skrives ut.
#Oppg.4.2.
# Hvis b<10 vil programmet gå inn i if-setningen og vi vil få error.
# Ellers vil ikke programmet støte på feilen.

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
