class Stasjon:
    def __init__(self,navn,reisemiddel):
        self._navn=navn
        self._reisemiddel=reisemiddel
        
    def hent_reisemiddel(self):
        return self._reisemiddel

def main():
    stasjonsbok={}
    for linje in open("stasjonstype.txt"):
        biter=linje.strip().split()
        navn=biter[0]
        typen=biter[1]
        stasjonsbok[navnet]=Stasjon(navn,typen)

    print(stasjonsbok["Moss"].hent_reisemiddel())
    interesse=stasjonsbok["Moss"]
    print(interesse)
    print(stasjonsbok["Moss"])
    #Begge de to siste linjene er like, de gir bare referansen til objektet.
    
