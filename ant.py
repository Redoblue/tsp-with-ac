class Ant:
    def __init__(self):
        self.pos = 0
        self.tabu = []
        self.dist = 0.0

    def reset(self):
        self.pos = 0
        self.tabu = []
        self.dist = 0.0
