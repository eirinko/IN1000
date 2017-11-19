def hastighet(fart):
    if fart<=60:
        return "fart:"+str(fart)
    else:
        return "fart:over 60"
    
print(hastighet(56))
print(hastighet(61))
print(hastighet(100))
