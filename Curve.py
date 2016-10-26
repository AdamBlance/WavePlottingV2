class Curve:
    steps = 20

    def __init__(self, distance):
        self.increment = (2*distance[0]) / (self.steps*(self.steps-1))
        self.initial_speed = distance*(self.steps-1)

        self.current_step = 0

    def start(self):
        pass

# don't use clamp - finish after steps have passed
