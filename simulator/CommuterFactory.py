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
        df = pd.read_csv(path, header=None).ffill(axis=0)
        df = df.astype('str')
        values = df.values

        commuterGoingList = []
        commDict = {}

        for row in values:

            if not row[2].isdigit():
                # skip filler
                continue

            # fucking z i don t know what that is
            if "Z" in row[2]:
                continue

            r2 = row[2]
            if r2[0] == '0':
                r2 = r2[1:]

            # they have commas in their numbers
            r4 = row[4].replace(",", "")

            r0 = row[0].replace(".0", "")

            # they have stars for anonym 1 or 2, so i just set it 2
            if r4 == "*":
                N = 2
                S = 2
            else:
                N = int(r4)
                S = int(r4)



            com = Commuter(N, S, 0, 0, r0, r2)
            if r0 in commDict:
                commuterGoingList.append(com)
            else:
                commuterGoingList = []
                commDict.update({r0: commuterGoingList})

        return commDict

    def loadLandKreise(self, path):
        self.irg
        self.irg2
        df = pd.read_csv(path, sep=';', header=None).astype('str')
        values = df.values
        sirDict: {str: SIRModel} = {}

        for row in values:
            ind = 7
            # get the latest counting
            while ind > 2 and not row[ind].isdigit():
                ind -= 1
            if ind <= 2:
                continue

            N = int(row[ind])
            S = N
            I = 0
            R = 0

            fromId = row[0]

            cODict: {str: Commuter} = {}
            nReduction = 0

            if fromId not in self.commuterDict.keys():
                self.irg = self.irg + 1
                print("FROMID NOT FOUND: " + fromId)
            else:
                commuterOutgoingList: [] = self.commuterDict[fromId]
                for commie in commuterOutgoingList:
                    self.irg2 = self.irg2 + 1
                    nReduction += commie.N
                    cODict.update({commie.idTo: commie})

            # id, N, S, I, R, commuter: {int: Commuter}
            sir = SIRModel(fromId, N - nReduction, S - nReduction, I, R, list(cODict.values()), row[1])
            assert sir.id not in sirDict, "id %s collission with %s: %s" % (sir.id, sirDict[sir.id].name, row)
            sirDict[sir.id] = sir

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

        self.loadAndSetStartingValue()

        return list(self.lkDict.values())

    def loadAndSetStartingValue(self):

        startingValues = pd.read_csv("pendlerData/start.csv")
        startingValues['id'] = startingValues['id'].astype('str')
        for start in startingValues.values:
            if start[0] in self.lkDict:
                lk = self.lkDict[start[0]]
                lk.S -= start[1]
                lk.S -= start[2]
                lk.I += start[1]
                lk.R += start[2]
            else:
                print("ID NOT FOUND FOR: " + start)


if __name__ == '__main__':
    cf = CommuterFactory()
    # cf.loadAll()
    cf.loadAndSetStartingValue()
