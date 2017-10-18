class Person():
    def __init__(self,navn):
        self._navn=navn
        self._status=None
        self._ektefelle=""
        self._navn_ektefelle=""

    def minStatus(self):
        if self._status!=None:
            print("Beklager, jeg er alt gift med {}.".format(self._navn_ektefelle))
        else:
            print("Jeg er paa sjekker'n.")

    def bryllup(self,ektefelle):
        self._ektefelle=ektefelle
        self._navn_ektefelle=ektefelle._navn
        self._status="gift"
