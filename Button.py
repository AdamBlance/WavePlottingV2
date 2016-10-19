import pygame
from pygame.locals import *
from GUIObject import GUIObject
pygame.font.init()


class Button(GUIObject):
    all_buttons = []
    button_text = pygame.font.Font('DejaVuSans.ttf', 15)
    offset = -30
    highlight_level = 20
    indent = -8
    text_padding = 12

    highlighted = pygame.Color(255, 162, 31)
    pressed = pygame.Color(75, 75, 75)

    def __init__(self, pos, colour, text, function, *args, size=None):
        self.depressed = False

        if size is not None:
            self.size = size
        else:
            text_size = self.button_text.size(text)
            self.size = (text_size[0] + self.text_padding, text_size[1] + self.text_padding)

        self.colour = colour
        self.function = function
        self.arguments = args

        self.state0 = pygame.Surface(self.size)  # None
        self.state1 = pygame.Surface(self.size)  # Moused over
        self.state2 = pygame.Surface(self.size)  # Pressed

        pygame.draw.rect(self.state0, self.pressed, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state0, colour, pygame.Rect((0, 0), self.size).inflate(self.indent, self.indent))

        pygame.draw.rect(self.state1, self.highlighted, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state1, colour, pygame.Rect((0, 0), self.size).inflate(self.indent, self.indent))

        pygame.draw.rect(self.state2, self.highlighted, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state2, self.pressed, pygame.Rect((0, 0), self.size).inflate(self.indent, self.indent))

        rendered_text = self.button_text.render(text, True, (255, 255, 255))
        super().__init__(pos, self.size)

        self.state0.blit(rendered_text, (self.text_padding/2, self.text_padding/2))
        self.state1.blit(rendered_text, (self.text_padding/2, self.text_padding/2))
        self.state2.blit(rendered_text, (self.text_padding/2, self.text_padding/2))

        self.all_buttons.append(self)

    def is_moused_over(self):
        mouse_pos = pygame.mouse.get_pos()
        moused_over = pygame.Rect(self.pos, self.size).collidepoint(mouse_pos)
        return moused_over

    def call_function(self):
        self.function(*self.arguments)

    def set_surface(self, mouse_event):
        mouse_bool = self.is_moused_over()
        if mouse_bool and mouse_event == MOUSEBUTTONDOWN:
            self.depressed = True
        elif mouse_bool and mouse_event == MOUSEBUTTONUP and self.depressed:
            self.depressed = False
            self.call_function()
        elif not mouse_bool:
            self.depressed = False

        if self.depressed and mouse_bool:
            self.blit(self.state2, (0, 0))
        elif mouse_bool:
            self.blit(self.state1, (0, 0))
        else:
            self.blit(self.state0, (0, 0))
