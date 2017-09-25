#Oppg.2.1. While-lokke som stanser ved inntasting av 0.

test=1
while test !=0:
    test=int(input("Skriv inn et tall: "))


#Oppg.2.2. lagre tall i tom liste.

test=1
tall=[]
while test !=0:
    test=int(input("Skriv inn et tall: "))
    tall.append(test)


#Oppg.2.3. for-lokke som skriver ut hvert element.

for i in range(len(tall)):
    print(tall[i])


#Oppg.2.4. minSum summerer tallene i listen.

sum=0
for i in range(len(tall)):
    sum+=tall[i]

print("Summen av tallene i listen er: ", sum)


#Oppg.2.5. finner min og maks i listen
#Forst minimum

minst=tall[0]
for i in tall:
    if i < minst:
        minst = i

#for i in range(1,len(tall)):
#    if minst>tall[i]:
#        minst=tall[i] to maater aa lose oppg paa.

print(minst)

#Deretter maks
maks=tall[0]
for i in tall:
    if i > maks:
        maks = i

print(maks)
