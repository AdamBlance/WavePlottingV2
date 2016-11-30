class Transition:
    steps = 20

    def __init__(self, pos, distance):

        self.original_pos = pos
        self.pos = pos
        self.extended_pos = pos + distance

        self.increment = (2*distance) / (self.steps*(self.steps+1))
        self.initial_speed = self.steps*self.increment
        self.value = 0

        self.in_use = False
        self.toggled = False

        self.current_step = 0

    def update(self):

        if self.in_use:

            self.current_step += 1
            if self.toggled:
                self.pos -= self.value
                self.value -= self.increment
            else:
                self.pos += self.value
                self.value -= self.increment

            if self.current_step > self.steps:

                self.current_step = 0
                self.value = 0
                self.in_use = False
                if self.toggled:
                    self.toggled = False
                    self.pos = self.original_pos
                else:
                    self.toggled = True
                    self.pos = self.extended_pos

    def start(self):
        self.in_use = True
        self.value = self.initial_speed
