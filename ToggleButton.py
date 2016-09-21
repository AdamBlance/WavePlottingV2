import pygame
from pygame.locals import *


class ToggleButton(pygame.Surface):
    all_toggle_buttons = []
    toggle_button_text = pygame.font.Font('DejaVuSans.ttf', 15)
    padding = 10
    text_colour = pygame.Color('#ebebeb')
    middle_colour = pygame.Color('#7c7a7a')
    mask_colour = (0, 0, 0)

    steps_until_toggled = 20

    def __init__(self, pos, colour1, colour2, text1, text2):

        self.slider_x = 0
        self.state = True
        self.pos = pos

        temp = False

        if self.toggle_button_text.size(text1) > self.toggle_button_text.size(text2):
            text_size1 = self.toggle_button_text.size(text1)
            text_size2 = self.toggle_button_text.size(text2)
        else:
            temp = True
            text_size1 = self.toggle_button_text.size(text2)
            text_size2 = self.toggle_button_text.size(text1)

        self.side_size = text_size1[0] + self.padding
        self.middle_size = text_size1[1]
        self.height = text_size1[1]
        self.toggle_length = self.side_size*2 + self.middle_size

        surface_size = (self.toggle_length + self.side_size, self.height)
        super().__init__(surface_size)

        self.pre_mask = pygame.Surface((self.toggle_length, self.height))

        pygame.draw.rect(self.pre_mask, colour1, pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.pre_mask, colour2, pygame.Rect((self.side_size + self.middle_size, 0), (self.side_size, self.height)))

        pygame.draw.rect(self.pre_mask, self.middle_colour, pygame.Rect((self.side_size, 0), (self.height, self.height)))
        rendered_text1 = self.toggle_button_text.render(text1, True, self.text_colour)
        rendered_text2 = self.toggle_button_text.render(text2, True, self.text_colour)

        if temp:  # Swaps sizes if larger text is first argument
            temp = text_size1
            text_size1 = text_size2
            text_size2 = temp

        self.pre_mask.blit(rendered_text1, ((self.side_size/2) - (text_size1[0]/2), 0))
        self.pre_mask.blit(rendered_text2, (self.side_size + self.middle_size + ((self.side_size/2) - (text_size2[0]/2)), 0))

        self.blit(self.pre_mask, (self.slider_x, 0))

        self.mask_layer = pygame.Surface(surface_size, SRCALPHA)

        pygame.draw.rect(self.mask_layer, self.mask_colour, pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.mask_layer, self.mask_colour, pygame.Rect((self.toggle_length, 0), (self.side_size, self.height)))

        self.blit(self.mask_layer, (0, 0))
        self.set_colorkey(self.mask_colour)

        self.increment = (2*self.side_size) / (self.steps_until_toggled*(self.steps_until_toggled-1))
        self.max_speed = (self.steps_until_toggled-1)*self.increment
        self.speed = 0
        self.toggled = False

    def is_moused_over(self):
        mouse_pos = pygame.mouse.get_pos()
        moused_over = pygame.Rect((self.pos[0] + self.side_size, self.pos[1]), (self.middle_size + self.side_size, self.height)).collidepoint(mouse_pos)
        return moused_over

    def redraw_surface(self):
        self.fill((0, 0, 0))
        self.blit(self.pre_mask, (self.slider_x, 0))
        self.blit(self.mask_layer, (0, 0))

    def turn_on(self):
        self.speed = self.max_speed
        self.toggled = True
        self.fill((0, 0, 0))
        self.blit(self.pre_mask, (self.slider_x, 0))
        self.blit(self.mask_layer, (0, 0))

    def turn_off(self):
        self.speed = -self.max_speed
        self.toggled = False

