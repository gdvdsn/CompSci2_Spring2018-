from npokergame import PokerApp
from ninterface import TextInterface
from nginterface import GraphicsInterface

inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
# activate choice buttons, deactivate others
