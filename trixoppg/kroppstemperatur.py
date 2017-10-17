def main():
    tempen=float(input("Skriv inn den maalte kroppstemperaturen din: \n"))
    if tempen<36.5:
        print("Din kroppstemperatur er under det som er normalt.")
    elif tempen >37.5:
        print("Din kroppstemperatur er over det som er normalt.")
    else:
        print("Din kroppstemperatur er normal.")

main()
