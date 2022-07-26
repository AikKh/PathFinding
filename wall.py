from Bases.baseSquare import BaseSquare, BLACK

class Wall(BaseSquare):

    def __init__(self, x, y):
        super().__init__(x, y, BLACK)
        
    def getText(self):
        return None