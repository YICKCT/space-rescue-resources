from GameFrame import Level
from Objects.Ship import Ship
from Objects.Zork import Zork
from GameFrame import Globals

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

            # add objects
        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self, Globals.SCREEN_WIDTH * 3/4, 25))