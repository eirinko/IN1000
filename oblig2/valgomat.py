#Lag en valgomat! Her er det endeløse muligheter for kompleksitet,
# men vi følger oppsettet til VG, som er ganske enkle ja/nei-spørsmål.
# Mulig dette ikke er så objektivt, og heller ikke så saklig.

navn=input("Hva heter du? Vi har ikke hemmelig valg her... \n")

svar1=input("1. Vi må øke skatter og avgifter for å opprettholde og bedre velferden vår. Svar: enig eller uenig. \n")

if svar1=="enig":
    print("Du er nok på venstresida i politikken, kamerat. \n")
elif svar1=="uenig":
    print("Du er nok på høyresida i politikken. På tide med ei lakrispipe. \n")
else:
    print("Nå må du se å ta et valg, enig eller uenig?!? \n")

svar2=input("2. Ja til at flere private aktører kan drive eldreomsorg, enig eller uenig? \n")

if svar2=="enig":
    print("Bestemor ut på anbud. HURRA!\n")
elif svar2=="uenig":
    print("Du likær'kke velferdsprofittører.\n")
else:
    print("Du må da ha meninger om alt, hvis du skal ta et valg?!? \n")

svar3=input("3. Det er bra med flere midlertidige ansettelser, enig eller uenig? \n")

if svar3=="enig":
    print("Så du liker at jobbsituasjonen er spennende og fleksibel i stedet for stabil? Deg om det...\n")
elif svar3=="uenig":
    print("LO liker deg.\n")
else:
    print("Trenger ikke jobb du, eller?\n")

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
