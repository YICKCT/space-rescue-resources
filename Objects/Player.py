from GameFrame import RoomObject
from Rooms import WelcomeScreen
import pygame

#Class for Player 
class Player(RoomObject): 
   def __init__(self, room, x, y): 
      RoomObject.__init__(self, room,x,y)
#image 
      image = self.load_image("Link.png")
      self.set_image (image,100,100)

      self.handle_key_events = True 

   def key_pressed(self, key):
      
      if key[pygame.K_w]:
         self.y -= 10

      elif key[pygame.K_s]:
         self.y += 10 
      
      elif key[pygame.K_d]:
         self.x += 10 

      elif key[pygame.K_a]:
         self.x -= 10 


#User input 
      #Register input 
      

   

   



