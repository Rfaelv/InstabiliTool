from ansys.mapdl.core import launch_mapdl
from mapdl_material import Material
from mapdl_finiteElement import FiniteElement
from mapdl_geomerty_I import IProfile
import sys

class Mapdl:
    def __init__(self, path):
        self.pathToLaunch = path

    def initialize(self):
        try:
            self.mapdl = launch_mapdl()
        except:
            print('ERROR-launch_mapdl')
            sys.exit()
        
    def getInstance(self):
        return self.mapdl

    def createMaterial(self, materialList):
        self.material = Material(self.mapdl)

        for i, material in enumerate(materialList):
            self.material.createMaterial(i + 1, material["materialType"], material["materialProperties"])
    
    def createFiniteElement(self):
        self.finiteElement = FiniteElement()
        self.finiteElement.createShell181(self.mapdl)
    
    def createProfile(self, profileProps):
        self.sectionType = profileProps[0]
        print('creatingProfile')
        if self.sectionType["I"]:
            print('seção I')
            self.Iprofile = IProfile(self.mapdl, profileProps[1])
            self.Iprofile.createSection()
            self.Iprofile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["tubular"]:
            return
        elif self.sectionType["C"]:
            return
        elif self.sectionType["C2"]:
            return
        elif self.sectionType["rack"]:
            return
        elif self.sectionType["angle"]:
            return
    
    def open_gui(self):
        self.mapdl.open_gui()
