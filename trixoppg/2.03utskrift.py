def main():
    radius=float(input("Skriv inn radius: "))
    diameter=2*radius
    areal=3.14*radius*radius
    omkrets=3.14*diameter
    tabell={"Diameter:":diameter,"Areal:":areal,"Omkrets:":omkrets}
    for parameter,verdi in tabell.items():
        print("{0:10} {1:.2f}".format(parameter,verdi))
    

main()
