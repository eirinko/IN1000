def main():
    passasjerer=int(input("Stasjon 1! Hvor mange gaar paa bussen? \n"))
    if passasjerer>30:
        pass_gaa=passasjerer-30
        passasjerer=30
        print("Bussen er full.",pass_gaa,"maa gaa til fots.")

    passasjerer=passasjerer+int(input("Stasjon 2! Hvor mange gaar paa bussen? \n"))
    if passasjerer>30:
        pass_gaa=passasjerer-30
        passasjerer=30
        print("Bussen er full.",pass_gaa,"maa gaa til fots.")

    passasjerer=passasjerer+int(input("Stasjon 3! Hvor mange gaar paa bussen? \n"))
    if passasjerer>30:
        pass_gaa=passasjerer-30
        passasjerer=30
        print("Bussen er full.",pass_gaa,"maa gaa til fots.")

main()
