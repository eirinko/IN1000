from ellevenullto_bil import Bil

class Person:
    def __init__(self,navn):
        self._mineBiler=[]
        self._laanteBiler=[]
        self._navn=navn

    def laanBil(self,bilen):
        if bilen.bilLedig()==False:
            print("Denne bilen er allerede utlaant.")
        else:
            bilen.laantBil()
            self._laanteBiler.append(bilen)
            print("Du faar laane ",bilen)
