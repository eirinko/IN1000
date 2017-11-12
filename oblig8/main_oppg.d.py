from node import Node
from rack import Rack
from regneklynge_d import Regneklynge

def main():
    abel=Regneklynge("regneklynge_test.txt")

    for i in range(len(abel.antNoder)):
        for j in range(abel.antNoder[i]):
            abel.settInnNode(Node(abel.minnePerNode[i],abel.listeProsessorAnt[i]))

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
