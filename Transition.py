class Transition:
    steps = 20

    def __init__(self, distance):
        self.increment = (2*distance) / (self.steps*(self.steps+1))
        self.initial_speed = self.steps*self.increment
        self.speed = 0

        self.in_use = False
        self.toggled = False

        self.is_negative = True
        self.current_step = 0

    def update(self):

        if self.in_use:
            self.current_step += 1
            if self.is_negative:
                self.speed -= self.increment
            else:
                self.speed += self.increment
            if self.current_step > self.steps:
                self.current_step = 0
                self.speed = 0
                self.in_use = False
                if self.toggled:
                    self.toggled = False
                else:
                    self.toggled = True

    def start(self, negative=False):
        self.in_use = True
        self.is_negative = negative
