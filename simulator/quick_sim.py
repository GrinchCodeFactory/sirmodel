from Commuter import Commuter
from SIRModel import SIRModel
from Simulation import runSimulation

'''
#N, S, I, R, idFrom, idTo
com1 = Commuter(10000, 9500, 400, 100, 0, 1)
com2 = Commuter(1000, 0, 0, 0, 1, 2)
com3 = Commuter(0, 0, 0, 0, 2, 1)
comList = [com1, com2, com3]


#id, N, S, I, R, commuter: [Commuter]):
sir1 = SIRModel(0,25000, 22700, 1050, 1250, {com1.idTo: com1})
sir2 = SIRModel(1,50000, 50000, 0, 0, {com2.idTo: com2})
sir3 = SIRModel(2,50000, 50000, 0, 0, {com3.idTo: com3})

# CHANGE TO DICT
sirList = {sir1.id:sir1, sir2.id:sir2, sir3.id:sir3}
'''


com1 = Commuter(N=10, S=10, I=0, R=0, idFrom=1, idTo=2)

sir1 = SIRModel(id=1, N=100, S=98, I=2, R=0, commuters=[com1], name="wohngebiet")
sir2 = SIRModel(id=2, N=100, S=100, I=0, R=0, commuters=[], name="industriegebiet")


runSimulation(
    sirList=[sir1, sir2],
    comList=[com1],
    days=20,
)


sir1.plot()
sir2.plot()

import matplotlib.pyplot as plt

plt.show()
