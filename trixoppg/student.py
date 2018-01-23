class Student:
    def __init__(self,navn,brukernavn,tlf):
        self._navn=navn
        self._brukernavn=brukernavn
        self._tlf=tlf

    def printInfo(self):
        print("Navn: ",self._navn)
        print("Brukernavn: ",self._brukernavn)
        print("Telefonnr: ",self._tlf)
