#Skal lage klassen celle.
class Celle:
    def __init__(self):
        self.settDoed()

    def settDoed(self):
        self._status=False


    def settLevende(self):
        self._status=True


    def erLevende(self):
        return self._status

    def hentStatusTegn(self):
        if self._status==True:
            return "O"
        else:
            return "."    
