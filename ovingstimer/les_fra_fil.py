# Filinnlesing

def hovedprogram():
    innfil=open("tekstfil.txt", "r")

    linje=innfil.readline()
    while linje!="":
        print(linje)
        linje=innfil.readline()
    innfil.close()

hovedprogram()
