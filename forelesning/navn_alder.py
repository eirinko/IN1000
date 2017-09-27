navn_alder_fil=open("alder.csv")

maksalder=0
eldst="Ingen"

for navn_alder in navn_alder_fil:
    biter=navn_alder_fil.split(":")
    navn=biter[0]
    alder=int(biter[1])
    if alder>maksalder:
        maksalder=alder
        eldst=navn

print(eldst)
