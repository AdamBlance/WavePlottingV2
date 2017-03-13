import TextContainer
from SpecialCharacter import SpecialCharacter


class Brackets(SpecialCharacter):

    padding = 8

    def __init__(self, event_manager, font_size):

        self.event_manager = event_manager

        self.contents = TextContainer.TextContainer(self.event_manager, font_size)

        super().__init__(self.event_manager, [self.contents])

    def render_symbol(self):

        self.contents.render_symbols()

        main_rect = self.contents.get_rect()

        backup = self.contents.font.size
        self.contents.font.size = (self.contents.font.size, main_rect.height)
        openb = self.contents.font.render('(', fgcolor=self.contents.colour)[0]
        closeb = self.contents.font.render(')', fgcolor=self.contents.colour)[0]
        self.contents.font.size = backup

        bracket_rect = openb.get_rect()
        contents_rect = self.contents.get_rect()

        super().reinit_surface((bracket_rect.width*2 + contents_rect.width + self.padding, contents_rect.height))

        self.blit(openb, (0, 0))
        self.blit(self.contents, (bracket_rect.width + self.padding/2, 0))
        self.blit(closeb, (contents_rect.width + bracket_rect.width + self.padding, 0))

    def update(self):

        self.contents.update()
        self.pointer_update()
