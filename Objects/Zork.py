from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from pygame import transform
import random 

class Zork(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        self.spawn_asteroid()

        self.rotate(90)
        
        # set inital movement
        self.y_speed = random.choice([-5,5])
        self.x_speed = random.choice([-5,5])

    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
        elif self.x + self.width > Globals.SCREEN_WIDTH or self.x < 0:
            self.x_speed *=-1 
        elif self.y > Globals.SCREEN_HEIGHT * 3/4:
            self.y_speed *=-1
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
    
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        asteroids = [
            Asteroid(self.room, self.x, self.y + self.height/2),
            Asteroid(self.room, self.x + self.width/2, self.y),
            Asteroid(self.room, self.x + self.width/2, self.y + self.height),
            Asteroid(self.room, self.x + self.height, self.y + self.width/2),

            Asteroid(self.room, self.x, self.y + self.height),
            Asteroid(self.room, self.x + self.width, self.y),
            Asteroid(self.room, self.x + self.width, self.y + self.height),
            Asteroid(self.room, self.x + self.height, self.y + self.width),
        ]

        for asteroid in asteroids:
            self.room.add_room_object(asteroid)

         # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(60, 120)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)



        