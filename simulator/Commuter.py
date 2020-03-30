class Commuter:
    N = 0
    S = 0
    I = 0
    R = 0

    idFrom = 0
    idTo = 0

    def __init__(self, N, S, I, R, idFrom, idTo):
        # print("init Commuter from:" + str(idFrom) + " to: " + str(idTo)+ " with N: " + str(N) + ", S: " + str(
        #   S) + ", I: " + str(I) + ", R: " + str(R))
        self.idFrom = idFrom
        self.idTo = idTo
        self.N = N
        self.S = S
        self.I = I
        self.R = R

        assert N == S + I + R

    def __str__(self):
        msg = "Commuter from: " + str(self.idFrom) + ", to: " + str(self.idTo) + "\n"
        msg += "Population: " + str(self.N) + "\n"
        msg += "Suseptible: " + str(self.S) + "\n"
        msg += "Infected: " + str(self.I) + "\n"
        msg += "Recovered: " + str(self.R) + "\n"
        return msg
