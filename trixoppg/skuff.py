class Skuff:
    def __init__(self):
        self._mineSokker=[]

    def settInnSokk(self,sokken):
        self._mineSokker.append(sokken)

    def sjekkStatus(self):
        antall_hoyresokker=0
        antall_venstresokker=0
        for sokk in self._mineSokker:
            if sokk.hentSide=="hoyre":
                antall_hoyresokker+=1
            elif sokk.hentSide=="venstre":
                antall_venstresokker+=1
                
        if antall_venstresokker==antall_hoyresokker:
            return "Alt i orden."
        else:
            return "Ulikt antall hoyre- og venstresokker."
