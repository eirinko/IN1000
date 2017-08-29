#Lag en valgomat! Her er det endeløse muligheter for kompleksitet,
# men vi følger oppsettet til VG, som er ganske enkle ja/nei-spørsmål.
# Bruk av prosedyre for å forenkle oppsettet er oppfordret. 

spm_teller=0

def spm(sporsmaal,enigtxt,uenigtxt,vetikke): #Henter inn spørsmål og resultatene som skrives ved de forskjellige valgene.
    global spm_teller
    spm_teller=spm_teller+1 #For å ha nummer foran spørsmålene.
    sporsmaal=str(spm_teller)+". "+sporsmaal #legger nummer foran spørsmålene.
    svar1=(input(sporsmaal)).lower() #sørger for at alle svarene gis i små bokstaver
    pos=["ja","enig","yes"] #gir en liste over positive svar
    neg=["nei","uenig","no"] #gir en liste over negative svar
    if svar1 in pos: #hvis svaret er positivt vil enigtxt skrives ut.
        print(enigtxt)
    elif svar1 in neg: #hvis svaret er negativt vil uenigtxt skrives ut.
        print(uenigtxt)
    else: #ellers vil brukeren få svar som om han eller hun er likegyldig.
        print(vetikke)

# Nedenfor kommer selve programmet
navn=input("Hva heter du? Vi har ikke hemmelig valg her... \n")

spm("Vi må øke skatter og avgifter for å opprettholde og bedre velferden vår. Svar: enig eller uenig. \n",
    "Du er nok på venstresida i politikken, kamerat. \n",
    "Du er nok på høyresida i politikken. På tide med ei lakrispipe. \n",
    "Er du helt likegyldig til dette, du da... \n")


spm("Ja til at flere private aktører kan drive eldreomsorg, enig eller uenig? \n",
    "Bestemor ut på anbud. HURRA, nå ble høyresida glad. \n",
    "Du likær'kke velferdsprofittører, nei. Venstresida. \n",
    "Du kan jo svare blank på valget 11. september også, men da kan du ikke klage på den politikken du får! \n")

spm("Det er bra med flere midlertidige ansettelser, enig eller uenig? \n",
    "Så du liker at jobbsituasjonen er spennende og fleksibel i stedet for stabil? Deg om det... Høyresidepolitikk, i alle fall.\n",
    "LO liker deg. Venstresida også. \n","Er jobb kjedelig? \n")

svar4=input("4. Team Erna eller team Jonas? Svar: Erna eller Jonas \n")

#if-setningen nedenfor passet ikke helt inn i prosedyren spm(), derfor valgte jeg å la den stå alene, men prinsippet er det samme som alle de over.
if svar4=="Erna":
    print("Fire nye år med det samme, altså. Høyresida av politikken.\n")
elif svar4=="Jonas":
    print("Greit så lenge han ikke konsekvensutreder for olje i LoVeSe. Venstresida av politikken. \n")
elif svar4=="Bjørnie":
    
    print("Du har helt rett. Dette er også et alternativ, dog sannsynligheten er lav for at det skjer..\n")
else:
    print("Pest eller kolera, tenker du kanskje. Det er jo et vanskelig valg. \n")

print("Uansett, lykke til på valgdagen 11. september, {}!".format(navn))
