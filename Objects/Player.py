from GameFrame import RoomObject
from Rooms import WelcomeScreen
import pygame

#Class for Player 
class Player(RoomObject): 
   def __init__(self, room, x, y): 
      RoomObject.__init__(self, room,x,y)

#image 
      image = Player.load_image("asteroid.png")
      self.set_image (WelcomeScreen(image,100,100))

#User input 
      #Register input 
      self.handle_key_events = True 
   def Input(self, key):
      if key[pygame.K_w]:
         self.y_speed = -10

      elif key[pygame.K_s]:
         self.y_speed = 10 
      
      elif key[pygame.K_a]:
         self.x_speed = 10 

      elif key[pygame.K_d]:
         self.x_speed = -10 


   




