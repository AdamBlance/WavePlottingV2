import pygame
from GUIObject import GUIObject
pygame.font.init()


class Sidebar(GUIObject):
    sidebar_text = pygame.font.Font('DejaVuSans.ttf', 20)
    steps_until_popped = 20

    def __init__(self, size, main_colour, tab_colour):
        self.x = -size[0]
        self.speed = 0
        self.popped_out = False
        self.size = size

        self.increment = (2*size[0]) / (self.steps_until_popped*(self.steps_until_popped+1))
        self.max_speed = self.steps_until_popped*self.increment
        print(self.increment, self.max_speed)

        super().__init__((0, 0), (size[0] + 10, size[1]))
        self.fill(main_colour)
        pygame.draw.rect(self, tab_colour, pygame.Rect((size[0], 0), (10, size[1])))

        expression_text = self.sidebar_text.render('Expressions:', True, pygame.Color('#ebebeb'))
        self.blit(expression_text, (0, 0))

        self.speed = self.max_speed
        self.popped_out = True

    def pop_in(self):
        self.speed = -self.max_speed
        self.popped_out = False

    def pop_out(self):
        self.speed = self.max_speed
        self.popped_out = True
