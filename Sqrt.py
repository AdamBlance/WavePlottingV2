import TextContainer
from SpecialCharacter import SpecialCharacter
import pygame


class Sqrt(SpecialCharacter):
    def __init__(self, event_manager, font_size):
        self.event_manager = event_manager

        self.contents = TextContainer.TextContainer(self.event_manager, font_size)

        super().__init__(self.event_manager, [self.contents])

    def render_symbol(self):

        self.contents.render_symbols()

        main_rect = self.contents.get_rect()

        backup = self.contents.font.size
        self.contents.font.size = (self.contents.font.size, main_rect.height + 1)
        rendered = self.contents.font.render('\u221a', fgcolor=self.contents.colour)[0]
        self.contents.font.size = backup

        root_rect = rendered.get_rect()

        total_height = main_rect.height + 2
        total_width = main_rect.width + root_rect.width
        super().reinit_surface((total_width, total_height))
        self.blit(rendered, (0, 0))
        self.blit(self.contents, (root_rect.width, 2))
        pygame.draw.line(self, self.contents.colour,
                         (root_rect.width, 0),
                         (root_rect.width + main_rect.width, 0))

    def update(self):

        self.contents.update()
        self.pointer_update()
