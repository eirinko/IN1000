maaneder=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
valgt_mnd=int(input("Hvilket nummer i rekka av maaneder vil du ha skrevet ut? \n"))-1

if valgt_mnd<0 or valgt_mnd>11:
    print("Tallet er ikke gyldig.")
else:
    print(maaneder[valgt_mnd])
