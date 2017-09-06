#Oppg.1.1: Skrive liste.
a=[1,2,3] #Oppretter liste.
a.append(4) #Legger til tallet 4 på slutten av lista.
print(a[0]) #Skriver ut det første tallet i lista.
print(a[2]) #Skriver ut det tredje tallet i lista.

#Oppg.1.2: Tom liste.
b=[] #Lager tom liste.

b.append(input("Du skal skrive inn fire navn totalt. \nSkriv inn et navn: ")) #Legger til det som er input "Navn", på slutten av lista.
b.append(input("Skriv inn et navn: ")) #Legger til det som er input "Navn", på slutten av lista.
b.append(input("Skriv inn et navn: ")) #Legger til det som er input "Navn", på slutten av lista.
b.append(input("Skriv inn et navn: ")) #Legger til det som er input "Navn", på slutten av lista.
#Fire navn har blitt lagt til på slutten av lista.

#Oppg.1.3: Sjekk om navn er med.
if "Eirin" in b:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Oppg.1.4: Slå sammen to lister.
c=a+b
print(c)

del c[-1] #fjern det siste elementet i liste c.
del c[-1] #fjern det siste elementet i liste c.

print(c)
