from GameFrame import RoomObject, Globals 
from Objects import Ship, Asteroid, Zork
import random

class Minizork(RoomObject):
    def __init__(self, room, x, y):

        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Zork.png")
        self.set_image(image,70,59)

        self.register_collision_object("Ship")

        angle = random.randint(45,135)
        self.set_direction(angle, 10)
       
        self.rotate(90)

        
    def step(self):

        self.keep_in_room()
        self.outside_of_room()

    def keep_in_room(self):
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1
        elif self.x < 0:
            self.x = 0 
            self.x_speed *= -1
        elif self.x + self.width > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width
            self.x_speed *= -1

    def minizork_explode(self): 
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

        boom = 6
        if boom == 6:
            print("minizork deleted")
            self.room.delete_object(self)
            
        

        explode_timer = (20)
        self.set_timer = (explode_timer, self.minizork_explode)
        
    def outside_of_room(self):

        if self.x + self.width < 0:
            print("mini zork deleted")
            self.room.delete_object(self)

    
    def handle_collision(self, other, other_type):

        
        if other_type == "Ship":
            self.room.running = False