import pygame
from Squares.target import Target

SCALE = 100
tX, tY = SCALE // 2, SCALE - 3
TARGET = Target(tX, tY)
REACHED = False

class BaseScreen:

    def __init__(self, size, count, caption: str):
        windowSize = size * count
        self.screen = pygame.display.set_mode((windowSize, windowSize))

        pygame.display.set_caption(caption)
        
        self.clock = pygame.time.Clock()
        self.fps = 60

        self._size = size
        self._count = count

        self._left = False
        self._right = False

    def onClick(self):
        self._left, _, self._right = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

        return x, y

    def draw(self):
        pass