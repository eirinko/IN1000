from sokk import Sokk
from skuff import Skuff

def main():
    sokk1=Sokk("venstre")
    sokk2=Sokk("venstre")
    sokk3=Sokk("hoyre")
    sokk4=Sokk("hoyre")
    skuff1=Skuff()

    skuff1.settInnSokk(sokk1)
    skuff1.settInnSokk(sokk2)
    skuff1.settInnSokk(sokk3)
    skuff1.settInnSokk(sokk4)

    skuff1.sjekkStatus()

main()
