def arverekke(forfader,etterkommer,forstefodte):
    rekken=[forfader]
    while rekken[-1] in forstefodte:
        rekken.append(forstefodte[rekken[-1]])
    if etterkommer not in rekken:
        rekken=[]
    return rekken

    
def main():
    barn={"Halfdan":"Harald","Christian":"Hans","Harald":"Eirik"}
    personer=arverekke("Halfdan","Eirik",barn)
    print(personer)
main()
