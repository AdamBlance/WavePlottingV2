import pygame
pygame.init()


class GUIObject(pygame.Surface):
    padding = 2

    # having padding in here is stupid

    main_font = pygame.font.Font('DejaVuSans.ttf', 15)
    font_colour = pygame.Color('#ebebeb')

    # todo: Add colour themes
    # todo: Make is_moused_over part of this class and override it in the ContextMenu class
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        super().__init__(size)
