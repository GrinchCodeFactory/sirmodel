import Commuter


##############################################################
##                                                          ##
## right now just fixed numbers, no distribution sampling   ##
## change in future for MCMC                                ##
##                                                          ##
##############################################################

class SIRModel:
    id = 0
    name = ""

    N = 0
    S = 0
    I = 0
    R = 0

    outgoingCommuters: {int: Commuter}

    NwC = 0
    SwC = 0
    IwC = 0
    RwC = 0

    beta = 0.00001
    gamma = 1 / 14

    timeStep = 0

    def __init__(self, id, N, S, I, R, commuter: {int: Commuter}, name="NO_NAME"):
        # print("init id: " + str(id) + ", name: "+ str(name) + " with N: " + str(N) + ", S: " + str(I) + ", I: " + str(I) + ", R: " + str(R))
        self.id = id
        self.name = name

        self.N = N
        self.S = S
        self.I = I
        self.R = R

        self.outgoingCommuters = commuter

        self.timeStep = 0

        self.sirSeries = []

    def dSus(self):
        return - 1 * self.beta * self.IwC * self.SwC

    def dInf(self):
        return self.beta * self.IwC * self.SwC - self.gamma * self.IwC

    def dRec(self):
        return self.gamma * self.IwC

    def nextTimeStep(self, commuter):

        # imitate day and night cycle
        dayTime = self.timeStep % 2 == 0

        self.includeCommuters(dayTime, commuter)

        # calculating the "ableitung" for the total number of ppl
        dS = self.dSus()
        dI = self.dInf()
        dR = self.dRec()

        servedN = 0

        # distribution of dS/dI/dR on basis vaules
        SN = self.S + (self.N / self.NwC) * dS
        if self.S == 0:
            servedN += self.N
        elif SN < 0:
            servedN += self.N * (SN / self.S)
        self.S = max(SN, 0)

        self.I = max(self.I + (self.N / self.NwC) * dI, 0)
        self.R = max(self.R + (self.N / self.NwC) * dR, 0)

        self.sirSeries.append((self.S, self.I, self.R))

        commie = commuter
        if not dayTime:
            commie = self.outgoingCommuters.values()
        # distribution of dS/dI/dR on commuters
        for c in commie:
            SC = c.S + (c.N / (self.NwC - servedN)) * dS
            if c.S == 0:
                servedN += c.N
            elif SC < 0:
                servedN += c.N * (SC / c.S)
            c.S = max(SC, 0)
            # c.S = max(c.S + (c.N / (self.NwC-servedS)) * dS, 0)
            if self.NwC - servedN == 0:
                continue
            c.I = max(c.I + (c.N / (self.NwC - servedN)) * dI, 0)
            c.R = max(c.R + (c.N / (self.NwC - servedN)) * dR, 0)

        self.timeStep += 1

        return commuter

    # add commuters from outside or add comuters coming home
    def includeCommuters(self, workingTime: bool, commuter: [Commuter]):
        self.NwC = self.N
        self.SwC = self.S
        self.IwC = self.I
        self.RwC = self.R

        # during the day the incoming comuters are considered
        if workingTime:
            for cIn in commuter:
                self.NwC += cIn.N
                self.SwC += cIn.S
                self.IwC += cIn.I
                self.RwC += cIn.R
        # during the night the outgoing comuters coming back are considered
        else:
            for key in self.outgoingCommuters:
                self.NwC += self.outgoingCommuters[key].N
                self.SwC += self.outgoingCommuters[key].S
                self.IwC += self.outgoingCommuters[key].I
                self.RwC += self.outgoingCommuters[key].R

    ##########################Setter and toString

    def setOutgoingCommuter(self, oCom: Commuter):
        self.outgoingCommuters[oCom.idTo] = oCom

    def setBeta(self, beta):
        self.beta = beta
        print("set beta to :" + str(self.beta))

    def setBeta(self, avgContactPerPerson, chanceToInfect):
        self.beta = avgContactPerPerson * chanceToInfect
        print("set beta to :" + str(self.beta))

    def setGamma(self, gamma):
        self.gamma = gamma
        print("set gamma to :" + str(self.gamma))

    def setGammaWithDuration(self, duration):
        self.gamma = 1 / duration
        print("set gamma to :" + str(self.gamma))

    def setGamma(self):
        self.gamma = self.R / self.I
        print("set gamma to :" + str(self.gamma))

    def plot(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        pd.DataFrame(self.sirSeries, columns=['S','I','R']).plot()
        plt.title(self.name)


    def __str__(self):
        msg = "SIRModel " + str(self.name) + " at t=" + str(self.timeStep / 2) + "\n"
        msg += "Population: " + str(self.N) + "\n"
        msg += "Suseptible: " + str(self.S) + "P(S): " + str(self.S / self.N) + "\n"
        msg += "Infected: " + str(self.I) + "P(I): " + str(self.I / self.N) + "\n"
        msg += "Recovered: " + str(self.R) + "P(R): " + str(self.R / self.N) + "\n"
        msg += "TotalCHECK: " + str(self.R + self.I + self.S) + "\n"
        return msg

        '''
        msg = "SIRModel at t=" + str(self.timeStep) + "\n"
        msg += "Population: " + str(self.NwC) + "\n"
        msg += "Suseptible: " + str(self.SwC) + "P(S): " + str(self.SwC / self.NwC) + "\n"
        msg += "Infected: " + str(self.IwC) + "P(I): " + str(self.IwC / self.NwC) + "\n"
        msg += "Recovered: " + str(self.RwC) + "P(R): " + str(self.RwC / self.NwC) + "\n"
        msg += "TotalCHECK: " + str(self.RwC + self.IwC + self.SwC) + "\n"
        '''
