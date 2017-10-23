def brillesjekk2(styrke):
    styrke[0]=1.75

pers_styrke=[1.5,1.5]
brillesjekk2(pers_styrke)
print(pers_styrke[0])

#Her refererer pers_styrke og styrke til samme listen.
#Naar brillesjekk2 endrer paa det referansen styrke peker til, endres ogsaa pers_styrke.
