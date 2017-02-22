import pygame
pygame.init()


class GUIObject(pygame.Surface):
    padding = 2

    # should only update objects if they need updated as blitting every frame is slow

    big_main_font = pygame.font.Font('DejaVuSans.ttf', 25)
    main_font = pygame.font.Font('DejaVuSans.ttf', 15)
    small_main_font = pygame.font.Font('DejaVuSans.ttf', 12)
    font_colour = pygame.Color('#ebebeb')

    # todo: Add colour themes
    # todo: Make is_moused_over part of this class and override it in the ContextMenu class
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        super().__init__(size)
