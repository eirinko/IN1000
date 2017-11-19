class Bud:
    def __init__(self,navn,budstorrelse):
        self._budgiver=navn
        if budstorrelse<=0:
            self._budStr=1
        else:
            self._budStr=budstorrelse
        
    def hentBudgiver(self):
        return self._budgiver
    
    def hentBudStr(self):
        return self._budStr
