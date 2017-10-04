#Oppg.5.1. Bruker oppgaveteksten som er gitt i oppgaven.
#Lager klassen Person.
class Person:
    def __init__(self,navn,alder):
        self._navn=navn
        self._alder=alder
        self._hobbyer=[]
#Har laget navn, alder og listen hobbyer.
        
#Skal lage metoden leggTilHobby.
    def leggTilHobby(self,Hobby):
        self._hobbyer.append(Hobby)

#Lager metoden skrivHobbyer.
    def skrivHobbyer(self):
        print(self._hobbyer)

#Lager en metode som skriver ut navn, alder og hobbyer.
    def skrivUt(self):
        print(self._navn)
        print(self._alder)
        self.skrivHobbyer()

#Lager hovedprogram og lar brukeren legge inn navn og alder.
def main():
    navn=input("Skriv inn navn: ")
    alder=int(input("Skriv inn alder: "))
    personObj=Person(navn,alder)

#Lage loop for aa legge til hobbyer.
    while input("Vil du legge til hobby, ja eller nei? ")=="ja":
        personObj.leggTilHobby(input("Legg til en hobby: "))

    personObj.skrivUt()
    
main()
