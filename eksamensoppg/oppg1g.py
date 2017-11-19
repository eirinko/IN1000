def brillesjekk(styrke):
    styrke[0]=1.75
    
pers_styrke=[1.5,1.5]
brillesjekk(pers_styrke)
print(pers_styrke[0])

def repeter(a):
    a=a+a
    return a

a="ab"
b=repeter(a)
print(a+b)
