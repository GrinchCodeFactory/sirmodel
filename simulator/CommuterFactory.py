import math
import pandas as pd

from Commuter import Commuter
from SIRModel import SIRModel


class CommuterFactory:
    commuterDict: {}
    lkDict: {}

    irg = 0
    irg2 = 0

    def __init__(self):
        self.commuterDict = {}
        lkDict: {}

    def loadCommuterRegion(self, path):
        df = pd.read_csv(path, header=None)
        values = df.values

        currentFromName = values[0,1]
        currentFromId = int(values[0,0])

        commuterGoingList = []
        commDict = {}

        for row in values:
            if math.isnan(row[0]):
                # they have commas in their numbers
                r4 = row[4].replace(",", "")
                # they have stars for anonym 1 or 2, so i just set it 2
                if r4 == "*":
                    N = 2
                    S = 2
                else:
                    N = int(r4)
                    S = int(r4)

                # fucking z i don t know what that is
                if "Z" in row[2]:
                    continue
                idTo = int(row[2])
                com = Commuter(N, S, 0, 0, currentFromId, idTo)

                commuterGoingList.append(com)
            else:
                if len(commuterGoingList) > 0:
                    commDict.update({currentFromId: commuterGoingList})
                    commuterGoingList = []

                currentFromId = row[0]
                currentFromName = row[1]
        return commDict

    def loadLandKreise(self, path):
        global irg
        global irg2
        df = pd.read_csv(path, sep=',|;', engine='python')
        values = df.values
        sirDict: {int: SIRModel} = {}

        for row in values:
            ind = 7
            # get the latest counting
            if isinstance(row[ind], float):
                row[ind] = str(row[ind])
            while ind > 3 and not row[ind].isdigit():
                ind -= 1
            if ind <= 3:
                continue

            N = int(row[ind])
            S = N  # at the moment everybudy is still healthy
            I = 0
            R = 0
            fromId = int(row[0])
            cODict: {int: Commuter} = {}

            if fromId not in self.commuterDict.keys():
                self.irg = self.irg + 1
            else:
                commuterOutgoingList: [] = self.commuterDict[fromId]
                for commie in commuterOutgoingList:
                    self.irg2 = self.irg2 + 1
                    cODict.update({commie.idTo: commie})

            # id, N, S, I, R, commuter: {int: Commuter}
            sir = SIRModel(fromId, N, S, I, R, cODict, row[1])
            sirDict.update({sir.id: sir})
        return sirDict

    def getCommuterList(self):
        result = []
        for comList in self.commuterDict.values():
            for com in comList:
                result.append(com)
        return result

    def loadAll(self):

        self.commuterDict = {}
        self.lkDict = {}

        for ind in range(1, 17):
            commuterDictTemp = self.loadCommuterRegion("pendlerData/pd" + str(ind) + ".csv")
            self.commuterDict.update(commuterDictTemp)

        print("Comuterlist loaded!  with " + str(len(self.commuterDict)))

        self.lkDict = self.loadLandKreise("pendlerData/BewohnerProLandkreis.csv")

        print("Notfound: " + str(self.irg) + ", Found: " + str(self.irg2))

        return self.lkDict


cf = CommuterFactory()
cf.loadAll()
