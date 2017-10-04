#Oppg.4.5. Lage hovedprogram der en hund opprettes.
#Maa foerst importere Hund-klassen.
from hund import Hund
def main():
    Amon=Hund(8,20,7)
#Hunden Amon loeper 7 ganger.
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())  
    Amon.spring()
    print("Vekt: ", Amon.returnerVekt())

#Hunden Amon spiser 7 ganger.
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    Amon.spis()
    print("Vekt: ", Amon.returnerVekt())
    
main()

