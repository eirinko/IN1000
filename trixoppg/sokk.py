class Sokk:
    def __init__(self,side):
        if side=="hoyre" or side=="venstre":
            self._side=side

    def hentSide(self):
        return self._side
