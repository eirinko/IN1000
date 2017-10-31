## Klasse for representasjon av regneklynge med racks og noder
#  MERK to alternative konstruktorer, avhengig av om oppgave d) loeses
from node import Node
from rack import Rack

class Regneklynge:
	## Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
	# @param noderPerRack max antall noder som kan plasseres i et rack
	def __init__(self, noderPerRack):
		self._noderPerRack=int(noderPerRack) #maks antall noder i et rack
		self._listeRacks=[]

	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om regneklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for regneklyngen ligger
#	def __init__(self, filnavn):
#		pass
# Kanskje jeg ser paa denne etterhvert.

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
                #Maa se gjennom lista av alle racks.
		if self._noderPerRack>self._listeRacks[-1].getAntNoder():
                        self._listeRacks[-1].append(node)
                else:
                        self._listeRacks.append(Rack())
                        self._listeRacks[-1].append(node)
                

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		self._prosessor_telling=0
		for element in self._listeRacks:
                        self._prosessor_telling+=element.antProsessorer()
                return self._prosessor_telling

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		self._NodeMinneIRacks=0
		for element in self._listeRacks:
                        self._NodeMinneIRacks+=element.noderMedNokMinne(paakrevdMinne)
                return self._NodeMinneIRacks

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return len(self._listeRacks)
