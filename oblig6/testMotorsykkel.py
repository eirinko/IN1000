#Oppg.2.5. Skal teste klassen som er opprettet. Importerer klassen.
from motorsykkel import Motorsykkel

#Oppg.2.6. Oppretter hovedprogram der jeg oppretter tre objekter og skriver ut.
def hovedprogram():
    Suzuki=Motorsykkel("Suzuki","DF1435",4500)
    Yamaha=Motorsykkel("Yamaha","VT1234",0)
    Vespa=Motorsykkel("Vespa","FT9876",10000)
    Suzuki.skrivUt()
    Yamaha.skrivUt()
    Vespa.skrivUt()

#Oppg.2.7. Skal oke kmStand for Vespa med 10 km, og sjekk at det er riktig.
#Skriv ut ved hjelp av hentKilometerstand.
    Vespa.kjor(10)
    print(Vespa.hentKilometerstand())

hovedprogram()

    
