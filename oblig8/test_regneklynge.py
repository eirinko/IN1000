from node import Node
from rack import Rack
from regneklynge import Regneklynge

def main():
    regneklynge1=Regneklynge(2)

    node1=Node(16,1)
    node2=Node(16,1)
    node3=Node(128,2)
    
    regneklynge1.settInnNode(node1)
    #print(regneklynge1.antRacks())
    regneklynge1.settInnNode(node2)
    #print(regneklynge1.antRacks())
    regneklynge1.settInnNode(node3)
    #print(regneklynge1.antRacks())
    #print(regneklynge1.antProsessorer())
    print(regneklynge1.noderMedNokMinne(32))
    
main()
