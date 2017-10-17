def main():
    broed=20
    melk=15
    ost=40
    yoghurt=12

    totalt=broed*int(input("Hei! Velkommen til IFI-butikken. \nHvor mange broed vil du ha? \n"))
    totalt=totalt+(melk*int(input("Hvor mange melk vil du ha? \n")))
    totalt=totalt+(ost*int(input("Hvor mange ost vil du ha? \n")))
    totalt=totalt+(yoghurt*int(input("Hvor mange yoghurt vil du ha? \n")))
    print("Du skal betale:",totalt,"kr")

main()
