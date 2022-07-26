import sys
from Bases.baseScreen import SCALE, TARGET
from Bases.baseSquare import *
from Squares.target import Target
from Squares.wall import Wall


sys.setrecursionlimit(max(1000, SCALE ** 2))

class Square(BaseSquare):

    #from A to square
    G = None

    #from B to square
    H = None

    _previousSquare = None

    reached = False

    @property
    def F(self):
        if self.G is not None:
            return self.G + self.H 
        return None


    def __init__(self, x: int, y: int):
        super().__init__(x, y, GREY)

        self.H = (abs(TARGET._x - x) * 10) + (abs(TARGET._y - y) * 4)

    
    def makeGreen(self, g, previousSquare):
        self._color = GREEN

        if self.G is None or g < self.G:
            self.G = g
            self._previousSquare = previousSquare
            
    # visit
    def makeRed(self, squares: list):
        self._color = RED

        for y in range(-1, 2):
            for x in range(-1, 2):
                if not (x == 0 and y == 0):
                    kX = self._x + x
                    kY = self._y + y

                    if 0 <= kX < SCALE and 0 <= kY < SCALE:
                        square = squares[kY][kX]
                        self.forEachSquare(square, x, y)

                        if Square.reached:
                            break
            if Square.reached:
                break


    def makeBlue(self):
        self._color = BLUE

        if self._previousSquare is not None:
            self._previousSquare.makeBlue()
                        

    def forEachSquare(self, square: BaseSquare, x, y):
        if type(square) == Target:
            self.makeBlue()
            Square.reached = True
            square._color = WHITE
        elif type(square) == Wall:
            return; 
        else:
            if square._color != RED and square._color != BLUE:
                g = 10 if x == 0 or y == 0 else 14
                valueG = g + self.G

                square.makeGreen(valueG, self)

    # def getText(self):
    #     middleC = SIZE // 2
    #     leftC = SIZE // 5
    #     rightC = SIZE - leftC
    #     if self.G is not None:
    #         f = getTextRect(self.F, bigFont, (self._x * SIZE + middleC, self._y * SIZE + middleC))
    #         s = getTextRect(self.G, smallFont, (self._x * SIZE + leftC, self._y * SIZE + leftC))
    #         t = getTextRect(self.H, smallFont, (self._x * SIZE + rightC, self._y * SIZE + leftC))

    #         return [f, s, t]
    #     return []
                        



    