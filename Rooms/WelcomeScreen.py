from GameFrame import Level 
from Objects.Title import Title

class WelcomeScreen(Level):
   
   def __init__(self, screen, joysticks):
      Level.__init__(self, screen, joysticks)

      self.set_background_image("Background.png")

    # add title object
      self.add_room_object(Title(self, 240, 200))