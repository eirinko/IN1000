from node import Node
from rack import Rack
from regneklynge import Regneklynge

def main():
    abel=Regneklynge(12)

    for i in range(650):
        abel.settInnNode(Node(64,1))

    # print(abel.antProsessorer()) en liten sjekk paa veien. Ble 650 prosessorer.

    for i in range(16):
        abel.settInnNode(Node(1024,2))

    min32=abel.noderMedNokMinne(32)
    min64=abel.noderMedNokMinne(64)
    min128=abel.noderMedNokMinne(128)
    antPros=abel.antProsessorer()
    antRack=abel.antRacks()

    print("Noder med minst 32 GB: ",min32)
    print("Noder med minst 64 GB: ",min64)
    print("Noder med minst 128 GB: ",min128)
    print("Antall prosessorer: ",antPros)
    print("Antall rack: ",antRack)
main()
