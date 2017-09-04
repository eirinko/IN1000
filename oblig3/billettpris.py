#Oppg.4.1.

def billett():
    alder=int(input("Hvor gammel er du? ")) #Definerer alder som input.
    billettpris=0 #Må definere variabelen før if-setningen.
    if alder<=17: #Sjekker om bruker er 17 år eller mindre.
        billettpris=30 #Barnepris
    elif alder>17 and alder<63: #Sjekker om bruker er mellom 17 og 63 år.
        billettpris=50 #Voksenpris
    else: #Da er det bare de over 63 år igjen.
        billettpris=35 #Pensjonistpris
    print("Prisen på din billett er {} kr.".format(billettpris)) #Skriver ut billettprisen.

# Oppg.4.5. Kaller på prosedyren 4 ganger etter hverandre.
billett()
billett()
billett()
billett()

# Oppg.4.6: Denne sjekker ikke at input er riktig.
# Hvis bruker skriver "tretten" som input vil ikke programmet skjønne at det er 13.
# Samme problemet oppstår med floats (f.eks. 13.5 år).
