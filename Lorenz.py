class Lorenz:
    def __init__(self, sigma, rho, beta, deltaT):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.deltat = deltaT
        self.set_initial(1.,1.,1.)

    def set_initial(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def iterate(self):
        newx = self.x + self.sigma * (self.y - self.x) * self.deltat
        newy = self.y + (self.x * (self.rho - self.z) - self.y) * self.deltat
        newz = self.z + (self.x * self.y - self.beta * self.z) * self.deltat
        self.x, self.y, self.z = newx, newy, newz
        return (self.x, self.y, self.z)
