#Oppg.4.1. lager tom liste inne i et hovedprogram og setter det paa slutten av fila.
#Oppg.4.2. Lager funksjonen slaaSammen.
def slaaSammen(str1,str2):
    return str1+str2

#sammenslaatt=slaaSammen("Hei du der",", du er kul")
#print(sammenslaatt)

#Oppg.4.3. Lager en prosedyre som heter skrivUt.
def skrivUt(ordliste):
    for i in ordliste:
        print(i)

#skrivUt(["hei","du","der"])

#Oppg.4.4. While-lokke
#Oppg.4.4.a. legger dette inn i hovedprogram

def hovedprogram():
    mineOrd=[]
    while input !="s":
        valg=input("Skriv inn ditt valg: i, u eller s.\n")
        if valg=="i":
            forlenge=slaaSammen(input("Skriv en tekststreng:\n"),input("Skriv en tekststreng til:\n"))
            mineOrd.append(forlenge)
        elif valg=="u":
            skrivUt(mineOrd)
        elif valg=="s":
            break
    print("Hoppet ut av programmet pga valg av s.")

hovedprogram()
