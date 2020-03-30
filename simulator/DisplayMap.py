import xml
import xml.etree.ElementTree as ET

from Commuter import Commuter
from SIRModel import SIRModel


class DisplayMap:
    tree: xml.etree.ElementTree.ElementTree
    root: ET.Element
    karte: ET.Element
    sirDict: {int, Commuter}

    def __init__(self, sirDict):
        self.tree = ET.parse('pendlerData/svgTest.svg')
        self.root = self.tree.getroot()
        self.karte = self.root[3][0]
        self.sirDict = sirDict


    def updateMap(self):
        for childK in self.karte:
            idFound = childK.attrib['id']

            if idFound.isdigit():
                idFound = int(idFound)
                red = 0
                if idFound in self.sirDict:
                    sm = self.sirDict[idFound]
                    red = int(255 * sm.I/sm.N)
                newVal = "fill: rgb("+str(red)+", 0, 0); stroke: rgb(76, 76, 76)"
                childK.attrib['style'] = newVal





    def saveMap(self, path):
        self.tree.write(path)

