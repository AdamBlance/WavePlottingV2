from SpecialCharacter import SpecialCharacter
from TextContainer import TextContainer


class Fraction(SpecialCharacter):

    line_padding = 7  # PPP|PPP
    side_padding = 8

    def __init__(self, event_manager, font_size, top=None, bottom=None):

        self.event_manager = event_manager
        self.numerator = top
        self.denominator = bottom
        self.numerator_container = TextContainer(self.event_manager, font_size)
        self.denominator_container = TextContainer(self.event_manager, font_size)

        bound_size = self.get_frac_size()
        super().__init__(self.event_manager, bound_size, font_size)

    def get_frac_size(self):
        blank_size = self.get_blank_size()
        if not self.numerator:
            top = blank_size
        else:
            top = self.numerator_container
        if not self.denominator:
            bottom = blank_size
        else:
            bottom = self.denominator_container

        total_height = top.height + self.line_padding + bottom.height
        total_width = max(top.width, bottom.width) + self.line_padding
        return total_width, total_height

