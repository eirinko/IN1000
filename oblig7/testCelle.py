from celle import Celle

def main():
    liv1=Celle()
    liv1.settLevende()
    print(liv1.erLevende())

    liv2=Celle()
    print(liv2.erLevende())

    print(liv1.tegnRepr())
    print(liv2.tegnRepr())
    
main()
