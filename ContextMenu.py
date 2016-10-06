import pygame


class ContextMenu(pygame.Surface):
    context_menu_text = pygame.font.Font('DejaVuSans.ttf', 15)
    padding = 0

    def __init__(self, pos, colour, entries):
        self.pos = pos
        self.colour = colour
        self.entries = entries

        index = 0
        max_len = len(entries[0].text)
        for i in range(1, len(entries)):
            current = len(entries[i].text)
            if current > max_len:
                max_len = current
                index = i

        print(self.context_menu_text.get_height())

        size = (self.context_menu_text.size(entries[index].text)[0],
                self.context_menu_text.get_height() * len(entries))

        super().__init__(size)
        self.fill(self.colour)

        text_alignment = 0
        for entry in entries:
            rendered_text = self.context_menu_text.render(entry.text, True, (255, 255, 255))
            self.blit(rendered_text, (0, text_alignment))
            if entries[-1] != entry:
                text_alignment +=  self.context_menu_text.get_height()
