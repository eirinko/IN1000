#Lag en valgomat! Her er det endeløse muligheter for kompleksitet,
# men vi følger oppsettet til VG, som er ganske enkle ja/nei-spørsmål.
# Mulig dette ikke er så objektivt, og heller ikke så saklig.

spm_teller=0

def spm(sporsmaal,enigtxt,uenigtxt,vetikke):
    global spm_teller
    spm_teller=spm_teller+1
    sporsmaal=str(spm_teller)+". "+sporsmaal
    svar1=(input(sporsmaal)).lower()
    pos=["ja","enig","yes"]
    neg=["nei","uenig","no"]
    if svar1 in pos:
        print(enigtxt)
    elif svar1 in neg:
        print(uenigtxt)
    else:
        print(vetikke)

navn=input("Hva heter du? Vi har ikke hemmelig valg her... \n")

spm("Vi må øke skatter og avgifter for å opprettholde og bedre velferden vår. Svar: enig eller uenig. \n",
    "Du er nok på venstresida i politikken, kamerat. \n",
    "Du er nok på høyresida i politikken. På tide med ei lakrispipe. \n",
    "Nå må du se å ta et valg, enig eller uenig?!? \n")


spm("Ja til at flere private aktører kan drive eldreomsorg, enig eller uenig? \n",
    "Bestemor ut på anbud. HURRA!\n",
    "Du likær'kke velferdsprofittører.\n",
    "Du må da ha meninger om alt, hvis du skal ta et valg?!? \n")

spm("Det er bra med flere midlertidige ansettelser, enig eller uenig? \n",
    "Så du liker at jobbsituasjonen er spennende og fleksibel i stedet for stabil? Deg om det...\n",
    "LO liker deg.\n","Trenger ikke jobb du, eller?\n")

svar4=input("4. Team Erna eller team Jonas? Svar: Erna eller Jonas \n")

if svar4=="Erna":
    print("Fire nye år med det samme? May the odds be ever in our favor.\n")
elif svar4=="Jonas":
    print("Greit så lenge han ikke konsekvensutreder for olje i LoVeSe.\n")
elif svar4=="Bjørnie":
    
    print("Du har helt rett. Dette hadde vært det beste alternativet.\n")
else:
    print("Ja, det er vanskelig med valg..\n")

print("Lykke til på valgdagen, 11. september, {}!".format(navn))
