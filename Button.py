import pygame
from GUIObject import GUIObject
pygame.font.init()


class Button(GUIObject):
    all_buttons = []

    highlighted = pygame.Color(255, 162, 31)
    pressed = pygame.Color(75, 75, 75)

    def __init__(self, event_manager, pos, colour, text, function, *args, size=None):

        indent = -6
        text_padding = abs(indent - self.padding)

        self.depressed = False
        self.event_manager = event_manager

        if size is not None:
            self.size = size
        else:
            text_size = self.main_font.size(text)
            self.size = (text_size[0] + 2*text_padding, text_size[1] + text_padding)

        self.colour = colour
        self.function = function
        self.arguments = args

        self.state0 = pygame.Surface(self.size)  # None
        self.state1 = pygame.Surface(self.size)  # Moused over
        self.state2 = pygame.Surface(self.size)  # Pressed

        pygame.draw.rect(self.state0, self.pressed, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state0, colour, pygame.Rect((0, 0), self.size).inflate(indent, indent))

        pygame.draw.rect(self.state1, self.highlighted, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state1, colour, pygame.Rect((0, 0), self.size).inflate(indent, indent))

        pygame.draw.rect(self.state2, self.highlighted, pygame.Rect((0, 0), self.size))
        pygame.draw.rect(self.state2, self.pressed, pygame.Rect((0, 0), self.size).inflate(indent, indent))

        rendered_text = self.main_font.render(text, True, (255, 255, 255))
        super().__init__(pos, self.size)

        self.state0.blit(rendered_text, (text_padding, text_padding/2))
        self.state1.blit(rendered_text, (text_padding, text_padding/2))
        self.state2.blit(rendered_text, (text_padding, text_padding/2))

        self.all_buttons.append(self)

    def is_moused_over(self):
        mouse_pos = pygame.mouse.get_pos()
        moused_over = pygame.Rect(self.pos, self.size).collidepoint(mouse_pos)
        return moused_over

    def call_function(self):
        self.function(*self.arguments)

    def update(self):
        moused_over = self.is_moused_over()
        if moused_over and self.event_manager.lmb_down:
            self.depressed = True
        elif moused_over and self.event_manager.lmb_up and self.depressed:
            self.depressed = False
            self.call_function()
        elif not moused_over:
            self.depressed = False

        if self.depressed:
            self.blit(self.state2, (0, 0))
        elif moused_over:
            self.blit(self.state1, (0, 0))
        else:
            self.blit(self.state0, (0, 0))
