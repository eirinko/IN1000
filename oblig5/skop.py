#Oppg.3.Skop. Skriver forst inn pogrammet.
def minFunksjon():
    for x in range(2):
        c=2
        print(c)
        c+=1
        b=10
        b+=a
        print(b)
    return(b)

def hovedprogram():
    a=42
    b=0
    print(b)
    b=a
    a=minFunksjon()
    print(b)
    print(a)

hovedprogram()

#Forst defineres minFunksjon, som ikke henter inn noen variabler.
#minFunksjon kjores ikke.
#BESKRIVELSE AV
#Denne har en for-lokke som gaar to ganger (x=0 og x=1).
#Forste iterasjon:
#c=2 og deretter skrives c ut (verdien 2)
#c blir lik 3.
#b blir lik 10.
#Deretter blir b satt til b+a, der b=10 og a ikke er definert.
#minFunksjon fungerer ikke og det kommer en feilmelding.

#Etter at minFunksjon er definert defineres hovedprogram().
#Inne i programmet blir a satt til 42.
#b blir satt til 0.
#Verdien til b skrives ut (0).
#b blir satt til a, dvs. at b=a=42.
#Naa kalles minFunksjon, men dette vil gi en feilmelding ved kjoring.
#Det betyr at print(b) og print(a) som staar nederst ikke blir kjort.

#Til naa har ingenting skjedd, men funksjonene har blitt definert.
#Paa den siste linjen staar det hovedprogram(), som vil kjore hovedprogrammet.

#Det folgende skjer:
#a=42
#b=0
#Verdien av b blir skrevet ut til skjermen (0).
#b=42
#a=minFunksjon, kaller paa minFunksjon,
#Forst skrives verdien til c ut (2)
#Resulterer i Error fra linjen der det staar b+=a, siden a ikke er definert.
