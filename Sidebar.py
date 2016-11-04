import pygame
from GUIObject import GUIObject
from Transition import Transition
pygame.font.init()


class Sidebar(GUIObject):
    sidebar_text = pygame.font.Font('DejaVuSans.ttf', 20)
    steps_until_popped = 20

    def __init__(self, size, main_colour, tab_colour):
        self.x = -size[0]
        self.size = size

        self.transition = Transition(size[0])

        super().__init__((0, 0), (size[0] + 10, size[1]))
        self.fill(main_colour)
        pygame.draw.rect(self, tab_colour, pygame.Rect((size[0], 0), (10, size[1])))

        expression_text = self.sidebar_text.render('Expressions:', True, pygame.Color('#ebebeb'))
        self.blit(expression_text, (0, 0))

    def update(self):
        self.transition.update()

    def pop_out(self):
        if not self.transition.in_use and not self.transition.toggled:
            self.transition.start(False)

    def pop_in(self):
        if not self.transition.in_use and self.transition.toggled:
            self.transition.start(True)
