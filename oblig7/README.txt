11.10.2017:
Starter med oppgaven.
Glemte aa skrive (self) etter definisjon av metodene, og fikk error.
Har skrevet self.settDoed() for aa ha metoden i bruk i konstruktoeren til klassen.
Ferdig med celle.py, ser ut til aa fungere som det skal.

Starter paa spillebrett.py

17.10.2017:
Jobbet med spillebrett.py. Gjorde ferdig punkt 5 under spillebrett.py.
Oensket at foerste generasjon skulle vaere nr. 0, derfor er self._generasjon satt til -1.
Ved bruk av metoden oppdatering() vil den bli 0 for foerste generasjon og oeke med 1 for hver generasjon.
Metoden oppdatering() fungerer som forventet.

18.10.2017:
Starter paa oppgave 6 under spillebrett.py, finnAntallLevende().
Ferdig med oppgave 6, og har skrevet kommentarer.
Har skrevet alt inn i main() og alt kjoerer som forventet.

Skrev forklarende tekst til celle.py

Forklaring til tegnBrett()
Startet med foelgende loesning av oppgaven:
#    def tegnBrett(self):
#        for i in range(self._rader):
#            for j in range(self._kolonner):
#                print(self._rutenett[i][j].hentStatusTegn(),end="")
#            print("")
Dette viste seg aa bruke veldig lang tid, spesielt med store brett.

Valgte derfor aa loese det paa denne maaten i stedet:
#    def tegnBrett(self):
#        for i in range(self._rader):
#            rad=""
#            for j in range(self._kolonner):
#                rad+=self._rutenett[i][j].hentStatusTegn()
#            print(rad)
Print() bruker veldig mye kapasitet og derfor er det ikke lurt aa bruke den saa mye.
Derfor er den andre loesningen bedre.

Forklaring til oppdatering():
