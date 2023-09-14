from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Minizork import Minizork 
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
        self.spawn_minizork()

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
        elif self.y + self.height > Globals.SCREEN_HEIGHT * 2/4:
            self.y_speed *=-1

    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()

    def spawn_minizork(self): 
        minizorks = [Minizork(self.room, self.x, self.y + self.height/2) ]

        for minizork in minizorks:
            self.room.add_room_object(minizork)

        minizork_spawn_time = (200)
        self.set_timer(minizork_spawn_time, self.spawn_minizork)
    
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        list = (1,2,3,4,5,6,7,8)
        
        spawned_asteroid = random.randint(1,8)

        print:("spawned_asteroid")

        if spawned_asteroid == 1: 
            self.room.add_room_object(Asteroid(self.room, self.x, self.y + self.height/2))
        elif spawned_asteroid == 2: 
            self.room.add_room_object(Asteroid(self.room, self.x + self.width/2, self.y))
        elif spawned_asteroid == 3: 
            self.room.add_room_object(Asteroid(self.room, self.x + self.width/2, self.y + self.height))
        elif spawned_asteroid == 4: 
            self.room.add_room_object(Asteroid(self.room, self.x + self.height, self.y + self.width/2))
        elif spawned_asteroid == 5: 
            self.room.add_room_object(Asteroid(self.room, self.x, self.y + self.height))
        elif spawned_asteroid == 6: 
           self.room.add_room_object(Asteroid(self.room, self.x + self.width, self.y))
        elif spawned_asteroid == 7:
            self.room.add_room_object(Asteroid(self.room, self.x + self.width, self.y + self.height))
        elif spawned_asteroid == 8:
            self.room.add_room_object(Asteroid(self.room, self.x + self.height, self.y + self.width))

         # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(60, 120)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)



        