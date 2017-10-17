class Emne:
    def __init__(self,emnekode,sem,stp): #kalles automatisk naar vi kaller en klasse.
        self._emnekode=emnekode
        self._semester=sem
        self._studiepoeng=stp*2 #studentene faar dobbelt poeng.

    def skrivUt(self): #Denne maa vi selv kalle paa.
        linje=(self._emnekode"("self._semester+"): "
               +str(self._studiepoeng)+" studiepoeng")
        print(linje)
        
