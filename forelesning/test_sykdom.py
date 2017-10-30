from sykdom import Sykdom

s=Sykdom("Kolera")

s.leggTilPosisjon(25)
s.leggTilPosisjon(30)

assert s.erAssosiert(30) #==True er implisitt.
assert s.erAssosiert(13)==False #Skal bli True, siden 13 ikke er assosiert.
