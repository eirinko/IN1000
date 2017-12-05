class Bil:
    def __init__(self,farge,merke):
        self._farge=farge
        self._merke=merke
        self._eier=""
        self._ledig=True

    def settEier(self,eier):
        self._eier=eier

    def laantBil(self):
        self._ledig=False

    def bilLedig(self):
        return self._laant

    def hvemEier(self):
        return self._eier
