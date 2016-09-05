import pygame
pygame.font.init()


class Sidebar(pygame.Surface):
    sidebar_text = pygame.font.Font('DejaVuSans.ttf', 15)
    steps_until_popped = 15

    def __init__(self, size, main_colour, tab_colour):
        self.x = -size[0]
        self.speed = 0
        self.popped_out = False
        self.size = size

        self.increment = (2*(size[0])) / (self.steps_until_popped*(self.steps_until_popped-1))
        self.max_speed = (self.steps_until_popped-1)*self.increment

        super().__init__((size[0] + 10, size[1]))
        self.fill(main_colour)
        pygame.draw.rect(self, tab_colour, pygame.Rect((size[0], 0), (10, size[1])))

    def pop_out(self):
        self.speed = self.max_speed
        self.popped_out = True

    def pop_in(self):
        self.speed = -self.max_speed
        self.popped_out = False
