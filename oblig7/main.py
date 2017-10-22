from spillebrett import Spillebrett

def main():
    rader=int(input("Hvor mange rader vil du at spillebrettet skal ha? \n"))
    kolonner=int(input("Hvor mange kolonner vil du at spillebrettet skal ha? \n"))

#Sjekker at bruker har valgt verdier storre enn 0.
    if (rader>0) and (kolonner>0):
        brett1=Spillebrett(rader,kolonner)
        while True:
            brett1.tegnBrett()
            brett1.oppdatering()
            print("Generasjon: {} - Antall levende celler: {}".format(brett1.generasjon(),brett1.finnAntallLevende()))
            svar=input("Press enter for aa fortsette eller q og enter for aa avslutte: ")
            if svar=="q":
                break
    else:
        print("Programmet kjoerer bare med positive verdier over 0. \nProev programmet igjen med positive verdier fra 1 og oppover.")

main()
