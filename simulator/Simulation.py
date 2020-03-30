import time
import timeit
from collections import defaultdict
from typing import List, Dict

from Commuter import Commuter
from CommuterFactory import CommuterFactory
from DisplayMap import DisplayMap
from SIRModel import SIRModel
from util.cpu_profiler import profiler_start, profiler_print

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


def runSimulation(days):
    counter = 1
    for i in range(2 * days):

        for sir in sirList.values():

            # find commuter coming to your city
            incCom = comByIdTo[sir.id]

            # iterate modle one step and get commuter after work
            newCom = sir.nextTimeStep(incCom)

            # this is only nessecary during work perio
            # distributing the newComs on the moddels
            if sir.timeStep % 2 == 0:
                for newC in newCom:
                    if (newC.idFrom == -1):
                        print("KEY -1 !!" + str(newC))
                    sirList[newC.idFrom].setOutgoingCommuter(newC)

        #print(sirList[1004])
        dm.updateMap()
        counter += 1
        dm.saveMap("out/output"+str(counter)+".svg")

def makePeopleSick():
    counter = 0
    for sir in sirList.values():
        if counter % 25 == 0:
            print("YOU GOT CORONA!")
            sir.I = 1000
            sir.S -= 1000
            counter += 1





cf = CommuterFactory()
sirList = cf.loadAll()
comList = cf.getCommuterList()

dm = DisplayMap(sirList)

comByIdTo: Dict[str, List[Commuter]] = defaultdict(list)
for com in comList:
    comByIdTo[com.idTo].append(com)

makePeopleSick()

t0 = time.perf_counter()

# profiler_start()

runSimulation(10)

# profiler_print()

t1 = time.perf_counter()

print('Simulation took %.2f seconds' % ((t1 - t0)))

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(367)
plot_keys = np.random.choice(list(sirList.keys()), 4, replace=False)
for k in plot_keys:
    sirList[k].plot()

plt.show()

