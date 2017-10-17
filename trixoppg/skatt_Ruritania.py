def main():
    inntekt=float(input("Skriv inn inntekten din: \n"))
    if inntekt<10000:
        skatt=inntekt*0.10
    elif inntekt>=10000:
        skatt=(10000*0.10)+((inntekt-10000)*0.30)
    print("Dette er beloepet som betales i skatt: ",skatt)
    
main()
