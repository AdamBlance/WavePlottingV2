import TextContainer
from SpecialCharacter import SpecialCharacter
import pygame


class NthRoot(SpecialCharacter):
    def __init__(self, event_manager, font_size):
        self.event_manager = event_manager

        self.contents = TextContainer.TextContainer(self.event_manager, font_size)
        self.nth_root = TextContainer.TextContainer(self.event_manager, font_size*0.6)

        super().__init__(self.event_manager, [self.nth_root, self.contents])

    def render_symbol(self):

        self.contents.render_symbols()
        self.nth_root.render_symbols()

        nth_rect = self.nth_root.get_rect()
        main_rect = self.contents.get_rect()

        backup = self.contents.font.size
        self.contents.font.size = (self.contents.font.size, main_rect.height + 1)
        rendered = self.contents.font.render('\u221a', fgcolor=self.contents.colour)[0]
        self.contents.font.size = backup

        root_rect = rendered.get_rect()

        total_width = nth_rect.width + root_rect.width + main_rect.width
        total_height = main_rect.height + nth_rect.height/2
        super().reinit_surface((total_width, total_height))

        self.blit(self.nth_root, (0, 0))
        self.blit(rendered, (nth_rect.width, nth_rect.height/2))
        self.blit(self.contents, (nth_rect.width + root_rect.width, nth_rect.height/2))
        pygame.draw.line(self, self.contents.colour,
                         (nth_rect.width + root_rect.width, nth_rect.height/2),
                         (nth_rect.width + root_rect.width + main_rect.width, nth_rect.height/2))

    def update(self):
        self.nth_root.update()
        self.contents.update()
        self.pointer_update()
