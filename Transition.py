class Transition:
    steps = 20

    # todo: option for exponential or logarithmic

    def __init__(self, distance):
        self.increment = (2*distance) / (self.steps*(self.steps+1))
        self.initial_speed = self.steps*self.increment
        self.speed = 0

        self.in_use = False
        self.toggled = False

        self.current_step = 0

    def update(self):

        if self.in_use:
            self.current_step += 1
            if self.toggled:
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

    def start(self):
        self.in_use = True
