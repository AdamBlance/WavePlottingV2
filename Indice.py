import TextContainer
from SpecialCharacter import SpecialCharacter


class Indice(SpecialCharacter):
    def __init__(self, event_manager, font_size):

        self.event_manager = event_manager

        self.indice = TextContainer.TextContainer(self.event_manager, font_size)

        super().__init__(self.event_manager, [self.indice])

    def render_symbol(self):

        self.indice.render_symbols()

        rect = self.indice.get_rect()
        total_height = rect.height*1.5

        super().reinit_surface((rect.width, total_height))

        self.blit(self.indice, (0, 0))

    def update(self):

        self.indice.update()
        self.pointer_update()
