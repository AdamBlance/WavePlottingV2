import pygame
from GUIObject import GUIObject
from Transition import Transition
pygame.font.init()


class Sidebar(GUIObject):
    sidebar_text = pygame.font.Font('DejaVuSans.ttf', 20)

    def __init__(self, size, main_colour, tab_colour):

        super().__init__([-size[0], 0], (size[0] + 10, size[1]))
        self.transition = Transition(self.pos[0], size[0])
        self.fill(main_colour)
        pygame.draw.rect(self, tab_colour, pygame.Rect((size[0], 0), (10, size[1])))

    def update(self):
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
