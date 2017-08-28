#Oppg. 1.1: Henter inn navn og bosted i to variabler. Skriver ut informasjonen i setning.
navn=input("Skriv inn navn: ")
bosted=input("Hvor kommer du fra? ")
print("Hei, {}! Du er fra {}.".format(navn, bosted))

#Oppg. 1.2: lager en prosedyre for oppg.1.1 som heter navnsted. Den kalles tre ganger.
def navnsted():
    navn=input("Skriv inn navn: ")
    bosted=input("Hvor kommer du fra? ")
    print("Hei, {}! Du er fra {}.".format(navn, bosted))

navnsted()
navnsted()
navnsted()
