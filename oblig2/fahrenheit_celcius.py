#Oppg. 2.1 Temp_F er temperaturen i Fahrenheit.
Temp_F=70

#Oppg.2.2. Skriver ut temperaturen i Fahrenheit.
print(Temp_F)

#Oppg. 2.3 Regner ut temperatur i Celcius.
Temp_C=(Temp_F-32)*5/9

#Oppg. 2.4 Skriver ut temperturen i Celcius.
print(Temp_C)

#oppg. 2.5 Her er det ikke tatt høyde for at folk kan skrive andre ting enn tall.
Temp_F=int(input("Hva er temperaturen i Fahrenheit? "))
print(Temp_F)
Temp_C=(Temp_F-32)*5/9
print(Temp_C)

#For å ta høyde for at folk kanskje skriver andre ting enn tall, kan vi f.eks. ha en if-setning som skriver ut en feilmelding hvis brukeren skriver noe annet.

