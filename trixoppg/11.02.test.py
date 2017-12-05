from ellevenullto_bil import Bil
from ellevenullto_person import Person

def main():
    dict_pers={}
    dict_pers["Eirin"]=Person("Eirin")
    dict_pers["Geir"]=Person("Geir")
    dict_pers["Mamma"]=Person("Mamma")

    dict_biler={}
    dict_biler["Mazda"]=Bil("gul","Mazda")
    dict_biler["Volvo"]=Bil("svart","Volvo")

    for key in dict_biler:
        key.settEier(dict_pers["Mamma"]) #Dukker opp feil.

    print(dict_biler["Volvo"].hvemEier())

main()
