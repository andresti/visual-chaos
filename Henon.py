class Henon:
    x = 0.5
    y = 0.5

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.deltat = 0.1

    def set_initial(self, x, y):
        self.x = x
        self.y = y

    def iterate(self):
        newx = 1 - self.a * self.x ** 2 + self.y
        newy = self.b * self.x
        self.x, self.y = newx, newy
        return (self.x, self.y)
