from Bases.baseSquare import BaseSquare, getTextRect, bigFont, BLUE



class Target(BaseSquare):

    def __init__(self, x, y):
        super().__init__(x, y, BLUE)

    # def getText(self):
    #     return [getTextRect('B', bigFont, (self._x * SIZE + 40, self._y * SIZE + 40))]

    