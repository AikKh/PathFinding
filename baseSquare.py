import pygame

SIZE = 8


GREY = (128, 128, 128)
GREEN = (20, 240, 0)
RED = (255, 0, 20)
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()
smallFont = pygame.font.Font('freesansbold.ttf', 8)
bigFont = pygame.font.Font('freesansbold.ttf', 12)

def getTextRect(string, font: pygame.font.Font, centerCors: tuple[int]):
    string = str(string)

    text = font.render(string[:5], True, WHITE)
    textRect = text.get_rect()

    textRect.center = centerCors
    return text, textRect


class BaseSquare:

    def __init__(self, x, y, color):
        self._x = x
        self._y = y

        self._color = color
        self.rect = pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE)


    def getText(self):
        pass
