class TallEn:
	def __init__(self, tall):
		self._mittTall = tall+1
	
	def hentVerdi(self):
		return self._mittTall

class TallTo:
	def __init__(self, tallEnObjekt):
		self._tallEnObjekt = tallEnObjekt
		self._mittTall = tallEnObjekt.hentVerdi() + 2

	def hentVerdi(self):
		return self._mittTall + self._tallEnObjekt.hentVerdi()

a = TallEn(1)
b = TallTo(a)
a = TallEn(b.hentVerdi())
b = TallTo(a)
print(b.hentVerdi())

def voks(alder):
        alder=alder+1

pers_alder=29
voks(pers_alder)
print(pers_alder)
