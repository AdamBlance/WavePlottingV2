import pygame
from GUIObject import GUIObject
from Transition import Transition
pygame.font.init()


class Sidebar(GUIObject):

    def __init__(self, size, main_colour, tab_colour):

        self.size = size

        self.colour = main_colour
        self.colourt = tab_colour

        self.size = size

        super().__init__([-size[0], 0], (size[0] + 10, size[1]))
        self.transition = Transition(self.pos[0], size[0])
        self.fill(main_colour)
        pygame.draw.rect(self, tab_colour, pygame.Rect((size[0], 0), (10, size[1])))

    def update(self):

        self.fill(self.colour)
        pygame.draw.rect(self, self.colourt, pygame.Rect((self.size[0]-10, 0), (11, self.size[1])))

        self.pos[0] = self.transition.pos

        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < 10:
            self.pop_out()
        elif mouse_pos[0] > self.size[0]:
            self.pop_in()
        self.transition.update()

    def pop_out(self):
        if not self.transition.in_use and not self.transition.toggled:
            self.transition.start()

    def pop_in(self):
        if not self.transition.in_use and self.transition.toggled:
            self.transition.start()
