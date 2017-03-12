import TextContainer
from SpecialCharacter import SpecialCharacter
import pygame


class Root(SpecialCharacter):
    def __init__(self, event_manager, font_size, has_nroot):
        self.event_manager = event_manager

        self.has_nroot = has_nroot

        if self.has_nroot:
            self.nth_root = TextContainer.TextContainer(self.event_manager, font_size*0.6)
        self.contents = TextContainer.TextContainer(self.event_manager, font_size)

        self.render_symbol()

        if self.has_nroot:
            super().__init__(self.event_manager, [self.nth_root, self.contents])
        else:
            super().__init__(self.event_manager, [self.contents])

    def render_symbol(self):

        if self.has_nroot:
            self.nth_root.render_symbols()
            nth_rect = self.nth_root.get_rect()
        self.contents.render_symbols()

        main_rect = self.contents.get_rect()

        backup = self.contents.font.size
        self.contents.font.size = (self.contents.font.size, main_rect.height + 1)
        rendered = self.contents.font.render('\u221a', fgcolor=self.contents.colour)[0]
        self.contents.font.size = backup

        root_rect = rendered.get_rect()

        if not self.has_nroot:
            total_height = main_rect.height + 2
            total_width = main_rect.width + root_rect.width
            super().reinit_surface((total_width, total_height))
            self.blit(rendered, (0, 0))
            self.blit(self.contents, (root_rect.width, 2))
            pygame.draw.line(self, self.contents.colour,
                             (root_rect.width, 0),
                             (root_rect.width + main_rect.width, 0))
        else:
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

        if self.has_nroot:
            self.nth_root.update()
        self.contents.update()
        self.pointer_update()
