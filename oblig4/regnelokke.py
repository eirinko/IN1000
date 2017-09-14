#Oppg.2.1. While-lokke som stanser ved inntasting av 0.

test=1
while test !=0:
    test=int(input("Skriv inn et tall: "))


#Oppg.2.2. lagre tall i tom liste.

test=1
listen=[]
while test !=0:
    test=int(input("Skriv inn et tall: "))
    listen.append(test)


#Oppg.2.3. for-lokke som skriver ut hvert element.

for i in range(len(listen)):
    print(listen[i])


#Oppg.2.4. minSum summerer tallene i listen.

sum=0
for i in range(len(listen)):
    sum+=listen[i]

print("Summen av tallene i listen er: ", sum)


#Oppg.2.5. finner min og maks i listen
#Forst minimum

minst=listen[0]
for i in listen:
    if i < minst:
        minst = i

for i in range(1,len(listen)):
    if minst>listen[i]:
        minst=listen[i]

#Deretter maks
maks=listen[0]
for i in listen:
    if i > maks:
        maks = i
