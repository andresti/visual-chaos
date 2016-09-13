class LotkaVolterra:
    x = 0.9
    y = 0.9

    def __init__(self, alpha, beta, gamma, delta, deltaT):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.deltaT = deltaT

    def set_initial(self, x, y):
        self.x = x
        self.y = y

    def iterate(self):
        newx = self.x + (self.alpha * self.x - self.beta * self.x * self.y)*self.deltaT
        newy = self.y + (self.delta * self.x * self.y - self.gamma * self.y)*self.deltaT
        assert(newx >= 0)
        assert(newy >= 0)
        self.x, self.y = newx, newy
        return (self.x, self.y)
