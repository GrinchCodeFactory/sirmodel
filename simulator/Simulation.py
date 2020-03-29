


from Commuter import Commuter
from CommuterFactory import CommuterFactory
from SIRModel import SIRModel

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
    for i in range(2*days):

        for sir in sirList.values():

            # find commuter coming to your city
            incCom = list(filter(lambda com: com.idTo == sir.id, comList))

            # iterate modle one step and get commuter after work
            newCom = sir.nextTimeStep(incCom)

            # this is only nessecary during work perio
            # distributing the newComs on the moddels
            if sir.timeStep % 2 == 0:
                for newC in newCom:
                    if(newC.idFrom==-1):
                        print("KEY -1 !!" + str(newC))
                    sirList[newC.idFrom].setOutgoingCommuter(newC)

        print(sirList[1004])


cf = CommuterFactory()
sirList = cf.loadAll()
comList = cf.getCommuterList()
runSimulation(5)


