from GameFrame import RoomObject

class Title(RoomObject):

    def __init__(self, room, x, y,):
        RoomObject.__init__(self, room, x, y,)
    
        # set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)