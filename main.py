from time import sleep
from autoFinding import AutoFinding
from Bases.baseScreen import TARGET, BaseScreen
from Bases.baseSquare import SIZE
from Bases.baseScreen import SCALE
from Squares.square import *
import pygame, sys

from labyrinthGenerator import LabyrinthGenerator

pygame.init()


class Board(BaseScreen):

    
    def __init__(self):
        global TARGET

        self._squares = [[Wall(x, y) for x in range(SCALE)] for y in range(SCALE)]

        lb = LabyrinthGenerator()
        startPos, targetPos = lb.createMap(self._squares)
        
        # target init
        TARGET._x, TARGET._y = targetPos
        TARGET.rect = pygame.Rect(TARGET._x * SIZE, TARGET._y * SIZE, SIZE, SIZE)
        self._squares[TARGET._y][TARGET._x] = TARGET
        #################


        # print(lb._stack)

        super().__init__(SIZE, SCALE, "Path finding")

        self._start = self._squares[startPos[1]][startPos[0]]  
        # self._start._color = WHITE 
        sleep(1)
        self._start.makeGreen(0, previousSquare = None) 

        self._auto = AutoFinding(self._squares)

    
    def draw(self):
        for y in self._squares:
            for sq in y:
                pygame.draw.rect(self.screen, sq._color, sq.rect)
                
                data = sq.getText()
                if data:
                    for text, textRect in sq.getText():
                        self.screen.blit(text, textRect)

    def onClick(self):
        x, y = super().onClick()
        x //= SIZE; y //= SIZE

        sq = self._squares[y][x]

        if self._left:
            
            if type(sq) == Square:
                if sq.G is not None:
                    sq.makeRed(self._squares)
                else:
                    self._squares[y][x] = Wall(x, y)  

        if self._right:
            if type(sq) == Wall:
                self._squares[y][x] = Square(x, y)


    def main(self):
        while True:
            self.onClick()

            self.screen.fill(BLACK)
            self.draw()
            pygame.display.flip() 

            self.clock.tick(self.fps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self._auto.is_alive():
                            self._auto.start()
                        
                    

if __name__ == "__main__":
    Board.main(Board()) 
