import time
from collections import defaultdict
from typing import List, Dict

from Commuter import Commuter
from CommuterFactory import CommuterFactory

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


def runSimulation(sirList, comList, days):
    t0 = time.perf_counter()

    comByIdTo: Dict[str, List[Commuter]] = defaultdict(list)
    for com in comList:
        comByIdTo[com.idTo].append(com)

    for i in range(2 * days):

        for sir in sirList:

            # find commuter coming to your city
            incCom = comByIdTo[sir.id]
            sir.nextTimeStep(incCom)


         # print(sirList[min(1004, len(sirList)])

    t1 = time.perf_counter()
    print('Simulation took %.2f seconds' % ((t1 - t0)))


def makePeopleSick(sirList):
    counter = 0
    for sir in sirList.values():
        if counter % 25 == 0 or True:
            print("YOU GOT CORONA!")
            sir.I = 1000
            sir.S -= 1000
            counter += 1


def main():
    cf = CommuterFactory()
    sirList = cf.loadAll()
    comList = cf.getCommuterList()

    makePeopleSick(sirList)

    runSimulation(sirList, comList, 60)

    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(367)
    plot_keys = np.random.choice(list(sirList.keys()), 4, replace=False)
    for k in plot_keys:
        sirList[k].plot()

    plt.show()


if __name__ == '__main__':
    main()
