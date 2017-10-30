from rack import Rack
from node import Node

def main():
    rack1=Rack()
    rack2=Rack()
    node1=Node(16,1)
    node2=Node(16,1)
    node3=Node(128,2)

    #tester alle funksjoner i Node():
    minnetest_node1=int(input("Hva er paakrevd minne for node 1? \n"))
    print(node1.nokMinne(minnetest_node1))

    minnetest_node2=int(input("Hva er paakrevd minne for node 2? \n"))
    print(node2.nokMinne(minnetest_node2))

    print(node1.antProsessorer())
    print(node2.antProsessorer())
    print(node3.antProsessorer())

    #tester funksjoner i Rack():
    rack1.settInn(node1)
    rack1.settInn(node2)
    rack2.settInn(node3)

    rack1_noder=rack1.getAntNoder()
    print(rack1_noder)
    rack1_pros=rack1.antProsessorer()
    print(rack1_pros)
    
    rack2_noder=rack2.getAntNoder()
    print(rack2_noder)
    rack2_pros=rack2.antProsessorer()
    print(rack2_pros)

    rack1_nokMinne=rack1.noderMedNokMinne(8)
    print(rack1_nokMinne)
    
    print(rack2.noderMedNokMinne(32))
main()
