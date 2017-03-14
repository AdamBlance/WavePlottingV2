from os.path import abspath
import pygame
import pygame.freetype
pygame.font.init()
pygame.freetype.init()


class GUIObject(pygame.Surface):
    padding = 2

    main_font = pygame.font.Font('media/DejaVuSans.ttf', 15)
    font_colour = pygame.Color('#ebebeb')

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        super().__init__(size)
