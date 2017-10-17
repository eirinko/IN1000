def main():
    a=int(input("Skriv inn et tall: \n"))
    if a<10:
        print("Tallet er under 10")
    elif 10<=a<=20:
        print("Tallet er mellom 10 og 20.")
    elif a>20:
        print("Tallet er storre enn 20.")

main()
