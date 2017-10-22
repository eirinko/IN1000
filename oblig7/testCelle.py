from celle import Celle
#Brukt til aa teste klassen Celle()

def main():
    liv1=Celle()
    liv1.settLevende()
    print(liv1.erLevende())

    liv2=Celle()
    print(liv2.erLevende())

    print(liv1.hentStatusTegn())
    print(liv2.hentStatusTegn())
    
main()
