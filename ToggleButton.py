import pygame
from pygame.locals import *
from GUIObject import GUIObject
from Transition import Transition


class ToggleButton(GUIObject):
    all_toggle_buttons = []
    middle_colour = pygame.Color('#7c7a7a')

    def __init__(self, pos, text1, text2):

        temp = False

        if self.main_font.size(text1) > self.main_font.size(text2):
            text_size1 = self.main_font.size(text1)
            text_size2 = self.main_font.size(text2)
        else:
            temp = True
            text_size1 = self.main_font.size(text2)
            text_size2 = self.main_font.size(text1)

        self.side_size = text_size1[0] + self.padding
        self.middle_size = text_size1[1]
        self.height = text_size1[1]
        self.toggle_length = self.side_size*2 + self.middle_size

        self.transition = Transition(self.side_size)

        surface_size = (self.toggle_length + self.side_size, self.height)
        super().__init__(pos, surface_size)

        self.pre_mask = pygame.Surface((self.toggle_length, self.height))

        pygame.draw.rect(self.pre_mask, pygame.Color(200, 0, 0), pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.pre_mask, pygame.Color(0, 200, 0), pygame.Rect((self.side_size + self.middle_size, 0),
                                                                             (self.side_size, self.height)))

        pygame.draw.rect(self.pre_mask, self.middle_colour, pygame.Rect((self.side_size, 0),
                                                                        (self.height, self.height)))
        rendered_text1 = self.main_font.render(text1, True, self.font_colour)
        rendered_text2 = self.main_font.render(text2, True, self.font_colour)

        if temp:  # Swaps sizes if larger text is first argument
            temp = text_size1
            text_size1 = text_size2
            text_size2 = temp

        self.pre_mask.blit(rendered_text1, ((self.side_size/2) - (text_size1[0]/2), 0))
        self.pre_mask.blit(rendered_text2,
                           (self.side_size + self.middle_size + ((self.side_size/2) - (text_size2[0]/2)), 0))

        self.mask_layer = pygame.Surface(surface_size, SRCALPHA)

        pygame.draw.rect(self.mask_layer, (0, 0, 0), pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.mask_layer, (0, 0, 0), pygame.Rect((self.toggle_length, 0),
                                                                 (self.side_size, self.height)))

        self.blit(self.mask_layer, (0, 0))
        self.set_colorkey((0, 0, 0))

    def is_moused_over(self):
        mouse_pos = pygame.mouse.get_pos()
        moused_over = pygame.Rect((self.pos[0] + self.side_size, self.pos[1]),
                                  (self.middle_size + self.side_size, self.height)).collidepoint(mouse_pos)
        return moused_over

    def toggle(self):
        self.transition.start()

    def update(self):

        self.pos[0] += self.transition.speed

        self.blit(self.pre_mask, (0, 0))
        self.blit(self.mask_layer, (0, 0))

        self.transition.update()
