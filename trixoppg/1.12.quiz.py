def trivia():
    spm=input("Hva heter hovedstaden i Marokko? \n")
    riktig=["Rabat","rabat","RABAT"]

    if spm in riktig:
        print("Helt rett!")
    else:
        print("Beklager, svaret var Rabat.")

trivia()
