#Oppg.2.1. Ordbok med butikkvarer og pris skal opprettes og printes.
diction={"melk":14.90,"brød":24.90,"yoghurt":12.90,"pizza":39.90}
print(diction)

#Oppg.2.2. Legg til to varer og print på nytt. Pris gitt fra brukeren.
#Lager en prosedyre for å legge til vare med verdi.
def leggtil(dict):
    vare1=input("Varenavn? ")
    verdi1=float(input("Verdi på varen? "))
    dict.update({vare1:verdi1})

#Prosedyren leggtil kalles to ganger og legger til vare+verdi på slutten av diction

leggtil(diction)
leggtil(diction)

print(diction)
#Usikker på tolkning av oppg., men gikk for input fra brukeren.
