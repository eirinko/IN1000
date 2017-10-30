from sykdomskatalog import SykdomsKatalog
from pasient import Pasient
katalog = SykdomsKatalog("sykdommer_test.csv")
pasient=Pasient("mutasjoner_test.tct")
for posisjon in pasient.alleMutasjoner():
    katalog.sjekkMutasjon(posisjon)
    
