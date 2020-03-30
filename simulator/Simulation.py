import time
from collections import defaultdict
from typing import List, Dict

from Commuter import Commuter
from CommuterFactory import CommuterFactory
from DisplayMap import DisplayMap


def runSimulation(sirList, comList, days, dm):
    t0 = time.perf_counter()

    sirDict = {s.id: s for s in sirList}

    comByIdTo: Dict[str, List[Commuter]] = defaultdict(list)
    for com in comList:
        comByIdTo[com.idTo].append(com)

    for i in range(2 * days):

        for sir in sirList:
            # find commuter coming to your city
            incCom = comByIdTo[sir.id]
            sir.nextTimeStep(incCom)

        print(sirDict[1004])

        if i % 2 == 0:
            dm.updateMap()
            dm.saveMap("out/output" + str(i) + ".svg")

    t1 = time.perf_counter()
    print('Simulation took %.2f seconds' % ((t1 - t0)))


def makePeopleSick(sirList):
    counter = 0
    for sir in sirList:
        if counter % 25 == 0:
            print("YOU GOT CORONA!")
            sir.I = 1000
            sir.S -= 1000
            counter += 1


def main():
    cf = CommuterFactory()
    sirList = cf.loadAll()
    comList = cf.getCommuterList()

    makePeopleSick(sirList)
    dm = DisplayMap(sirList)

    runSimulation(sirList, comList, days=40, dm=dm)

    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(367)
    for s in np.random.choice(sirList, 4, replace=False):
        s.plot()

    plt.show()


if __name__ == '__main__':
    main()
