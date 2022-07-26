from threading import Thread
from Bases.baseScreen import REACHED
from Bases.baseSquare import GREEN
from Squares.square import Square
from time import sleep


class AutoFinding(Thread):

    def __init__(self, squares: list[Square]):
        super().__init__()

        self._squares = squares

    def getGreens(self):
        return [s for y in self._squares for s in y if s._color == GREEN]


    def run(self):
        global REACHED

        while not Square.reached:
            greens = self.getGreens()


            smallest = min(greens, key = lambda sq: sq.F)

            smallests = [square for square in greens if square.F == smallest.F]

            for sm in smallests:
                sm.makeRed(self._squares)

            # sleep(0.01)
