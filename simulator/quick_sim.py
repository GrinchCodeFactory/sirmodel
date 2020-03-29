from Commuter import Commuter
from SIRModel import SIRModel
from Simulation import runSimulation

com1 = Commuter(N=10, S=10, I=0, R=0, idFrom=1, idTo=2)

sir1 = SIRModel(id=1, N=100, S=98, I=2, R=0, commuters=[com1], name="wohngebiet")
sir2 = SIRModel(id=2, N=100, S=100, I=0, R=0, commuters=[], name="industriegebiet")


runSimulation(
    sirList=[sir1, sir2],
    comList=[com1],
    days=50,
)


sir1.plot()
sir2.plot()

import matplotlib.pyplot as plt

plt.show()
