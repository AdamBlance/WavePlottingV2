import pygame
from pygame.locals import *
from GUIObject import GUIObject
from Transition import Transition


class ToggleButton(GUIObject):
    all_toggle_buttons = []
    middle_colour = pygame.Color('#7c7a7a')

    def __init__(self, event_manager, size, pos, text1, text2):

        self.event_manager = event_manager

        self.was_clicked = False
        self.depressed = False
        self.width = size[0]
        self.height = size[1]

        self.side_size = (self.width - self.height) + 2*self.padding
        self.middle_size = self.height
        self.height = self.height
        self.toggle_length = 2*self.side_size + self.middle_size

        self.transition = Transition(0, self.side_size)

        surface_size = (self.toggle_length + self.side_size, self.height)
        super().__init__(pos, surface_size)

        self.rendered_text1_size = self.main_font.size(text1)
        self.rendered_text2_size = self.main_font.size(text2)

        self.pre_mask = pygame.Surface((self.toggle_length, self.height))
        self.pre_mask_x = 0

        pygame.draw.rect(self.pre_mask, pygame.Color(200, 0, 0), pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.pre_mask, pygame.Color(0, 200, 0), pygame.Rect((self.side_size + self.middle_size, 0),
                                                                             (self.side_size, self.height)))

        pygame.draw.rect(self.pre_mask, self.middle_colour, pygame.Rect((self.side_size, 0),
                                                                        (self.height, self.height)))

        rendered_text1 = self.main_font.render(text1, True, self.font_colour)
        rendered_text2 = self.main_font.render(text2, True, self.font_colour)

        self.pre_mask.blit(rendered_text1, ((self.side_size/2)-self.rendered_text1_size[0]/2,
                                            (self.height/2)-(self.rendered_text1_size[1]/2)))
        self.pre_mask.blit(rendered_text2,
                           (self.side_size + self.middle_size + (self.side_size/2)-self.rendered_text2_size[0]/2,
                            (self.height/2)-(self.rendered_text1_size[1]/2)))

        self.mask_layer = pygame.Surface(surface_size, SRCALPHA)

        pygame.draw.rect(self.mask_layer, (0, 0, 0), pygame.Rect((0, 0), (self.side_size, self.height)))
        pygame.draw.rect(self.mask_layer, (0, 0, 0), pygame.Rect((self.toggle_length, 0),
                                                                 (self.side_size, self.height)))

        self.set_colorkey((0, 0, 0))

    def is_moused_over(self):
        mouse_pos = pygame.mouse.get_pos()
        moused_over = pygame.Rect((self.pos[0] + self.side_size, self.pos[1]),
                                  (self.middle_size + self.side_size, self.height)).collidepoint(mouse_pos)
        return moused_over

    def toggle(self):
        if not self.transition.in_use:
            self.was_clicked = True
        self.transition.start()

    def update(self):

        self.was_clicked = False
        moused_over = self.is_moused_over()
        if moused_over and self.event_manager.lmb_down:
            self.depressed = True
        elif moused_over and self.event_manager.lmb_up and self.depressed:
            self.depressed = False
            self.toggle()
        elif not moused_over:
            self.depressed = False

        self.pre_mask_x = self.transition.pos

        self.blit(self.pre_mask, (self.pre_mask_x, 0))
        self.blit(self.mask_layer, (0, 0))

        self.transition.update()
