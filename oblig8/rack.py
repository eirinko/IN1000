## Klasse for representasjon av racks i en regneklynge.
#
from node import Node
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		self._listeNoder=[]

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self._listeNoder.append(node)

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self._listeNoder)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		self._prosessor_telling=0
		for element in self._listeNoder:
                        self._prosessor_telling+=element.antProsessorer()
                return self._prosessor_telling                

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		self._nokMinne=0
		for element in self._listeNoder:
                        if element.nokMinne==True:
                                self._nokMinne+=1
                return self._nokMinne
