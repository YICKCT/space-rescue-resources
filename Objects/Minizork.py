from GameFrame import RoomObject, Globals 
from Objects import Ship 
import random

class Minizork(RoomObject):
    def __init__(self, room, x, y):

        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Zork.png")
        self.set_image(image,70,59)

        traker  = Ship.x, Ship.y
        self.set_direction(traker, 10)

        self.register_collision_object("Ship")

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

    
    def outside_of_room(self):

        if self.x + self.width < 0:
            print("mini zork deleted")
            self.room.delete_object(self)

    
    def handle_collision(self, other, other_type):

        
        if other_type == "Ship":
            self.room.running = False