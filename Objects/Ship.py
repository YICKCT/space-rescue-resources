from GameFrame import RoomObject, Globals
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)

        self.rotate(90)

        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y -= 100
        elif key[pygame.K_s]:
            self.y += 100
        elif key[pygame.K_a]:
            self.x -= 100
        elif key[pygame.K_d]:
            self.x += 100

    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        elif self.x < 0:
            self.x = 0 
        elif self.x + self.width > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
        

    
