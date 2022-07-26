from random import randrange
import pygame
from Bases.baseScreen import SCALE, BaseScreen
from Bases.baseSquare import WHITE
from Squares.square import Square
from Squares.wall import Wall


class LabyrinthGenerator:

    length = (SCALE // 3) - 1
    
    _stack = []
    visitedList = []
    

    def setStack(self):

        startPos = (0, 0)
        outOf = lambda i: not (0 <= i < self.length)

        def step(pos: tuple[int, int], b = False):
            self._stack.append(pos)
            self.visitedList.append(pos) 

            if pos != startPos or b:#len(self.visitedList) < self.maxCount:
                px, py = pos

                nearCors = [(px + x, py + y) for x, y in [(1, 0), (0, 1), (0, -1), (-1, 0)] if not outOf(px + x) and not outOf(py + y)]
                unvisited = [nearCor for nearCor in nearCors if nearCor not in self.visitedList]


                if len(unvisited) > 0:
                    nextPos = unvisited[randrange(len(unvisited))]
                    return step(nextPos)
                else:
                    self._stack.pop()
                    # self.visitedList.pop()
                    return step(self._stack.pop())

        step(startPos, True)
        self._stack = [(x * 3 + 2, y * 3 + 2) for x, y in self.visitedList]



    def createMap(self, squares: list[list]):
        self.setStack()
        getSign = lambda x, y: 1 if x > y else -1
        #squares = [[Wall(x, y) for x in range(len(SCALE))]for y in range(len(squares))]
        resCors = []

        for i in range(len(self._stack) - 2):
            pX, pY = self._stack[i]
            nX, nY = self._stack[i + 1]

            rangeX = range(pX, nX, getSign(nX, pX)) if nX != pX else [nX, nX, nX]
            rangeY = range(pY, nY, getSign(nY, pY)) if nY != pY else [nY, nY, nY]
            for x, y in zip(rangeX, rangeY):
                resCors.append((x, y))


        resCors = list(set(resCors))
        
        for x, y in resCors:
            squares[y][x] = Square(x, y)

        return self._stack[0], self._stack[randrange(0, len(self._stack) - 1)]

        

if __name__ == "__main__":
    lb = LabyrinthGenerator()
    lb.setStack()
    print("-------------------------------")
    print(lb._stack)


            

            