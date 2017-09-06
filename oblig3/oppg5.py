#Oppg.5: Oppgavetekst, med lister
# 1. Lag en tom liste.
# 2. Legg til tre elementer i slutten av lista.
# 3. Legg til et element som første element av lista.
# 4. Legg til et element som andre element av lista.
# 5. Sorter listen, stigende rekkefølge. OBS! Har det blitt lagt inn num, int eller str?# I deloppg. 5 skal tall komme først, deretter str. i alfabetisk rekkefølge.
#oppg.5.1.liste=[]
print(liste)
#Oppg.5.2.liste.append("ananas")liste.append(2)liste.append("nam")
print(liste)
#Oppg.5.3.liste.insert(0,3)
print(liste)
#Oppg.5.4.liste.insert(1,"fem")
print(liste)
#Oppg.5.5#liste=sorted(liste) hadde fungert om alle elementene i lista var av samme type.#int må gjøres om til str for at disse skal kunne sammenlignes.
for i in range(len(liste)): #for-løkken gjør om int's til str's.    liste[i]=str(liste[i])
print(liste) #for å vise listen med strings.
liste=sorted(liste) #sorterer lista og lagrer det i navnet liste.print(liste)
