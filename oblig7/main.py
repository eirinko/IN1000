from spillebrett import Spillebrett

def main():
    brett1=Spillebrett(10,20)
 
    while True:
        brett1.oppdatering()
        brett1.tegnBrett()
        print("Generasjon: {} - Antall levende celler: {}".format(brett1.generasjon(),"antall levende"))
        svar=input("Press enter for aa fortsette eller q og enter for aa avslutte: ")
        if svar=="q":
            break

main()
