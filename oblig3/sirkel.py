#Oppg.3.1-4. Bruke modulen ezGraphics.py for å tegne figurer. Har dessverre ikke fått meg pensumboka enda...
#Henter først ut GraphicsWindow fra exgraphics, der figurene kan tegnes.

from ezgraphics import GraphicsWindow

# Lage et vindu for å tegne i, 500x500 pixels.
vindu = GraphicsWindow(500, 500)

# Setter tittel på vinduet.
vindu.setTitle("Oppg. 3: Rød sirkel")

#Gir navn til vinduet for å bruke videre i programmeringen.
canvas = vindu.canvas()

#Gir sirkelen rødfarge.
canvas.setOutline("red")

#canvas.setFill("red") #kan brukes for å lage det japanske flagget.

#canvas.drawOval(x, y, width, height) brukes for å tegne sirkel.
canvas.drawOval(100,100,300,300)
