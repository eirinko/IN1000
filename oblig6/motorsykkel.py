#Oppg. 2.1. definerer en klasse for motorsykler, der den henter inn merke, regnr og km-stand.
#Antar at km-stand starter paa 0. 
class Motorsykkel:
    def __init__(self,merke,regnr,kmStand):
        self._merke=merke
        self._regnr=regnr
        self._kmStand=kmStand

#Oppg.2.2. Kjor-metoden oeker km-standen med det som blir skrevet inn.
    def kjor(self,km):
        self._kmStand+=km

#Oppg.2.3. Skriver en metode for aa hente ut kmStand-verdien, i lagret i return-variabelen.
    def hentKilometerstand(self):
        return self._kmStand


#Oppg.2.4. Skriver en metode skrivUt(self) for aa skrive ut merke, registreringsnummer og kmStand.
    def skrivUt(self):
        print("Motorsykkelmerket er: ", self._merke)
        print("Registreringsnummeret til motorsykkelen er: ",self._regnr)
        print("Kilometerstanden til motorsykkelen er: ", self._kmStand)
        

    
