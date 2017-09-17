#Oppg.3.1. lage grafikkvindu win og kanvas can.

from ezgraphics import GraphicsWindow

win = GraphicsWindow(500, 500)
can = win.canvas()

#Oppg.3.2. Oppretter to variabler: teller = 0 og x_pos = 10.

teller = 0
x_pos = 10


#Oppg.3.3. while-lokke, for teller<9

#while teller <9:
#    can.drawOval(x_pos, 100, 50, 50)
#    teller+=1
#    x_pos+=10

#Oppg.3.4. stoerrelsen paa sirklene er avhengig av variablen stoerrelse,
#som oker med 5 for hver runde i while-lokken.
stoerrelse=100
while teller <9:
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    teller+=1
    x_pos+=6
    stoerrelse+=5
