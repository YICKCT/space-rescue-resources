from GameFrame import Level
from Objects.Player import Player 

class WelcomeScreen(Level):
 def __init__(self, screen, joysticks):
    Level.__init__(self, screen, joysticks)

    #Background image 
    image = self.set_background_image("totk.png")
    
    #Add player 
    self.add_room_object(Player(self, 25,50))
