import pygame
pygame.init()


class GUIObject(pygame.Surface):
    padding = 2
    main_font = pygame.font.Font('DejaVuSans.ttf', 15)
    font_colour = pygame.Color('#ebebeb')

    # todo: Add colour themes

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        super().__init__(size)
