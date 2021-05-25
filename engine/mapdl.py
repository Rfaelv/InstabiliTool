from ansys.mapdl.core import launch_mapdl
from mapdl_material import Material
from mapdl_finiteElement import FiniteElement
from mapdl_geometry_I import IProfile
from mapdl_geometry_tubular import TubularProfile
from mapdl_geometry_C import CProfile
from mapdl_geometry_C2 import C2Profile
from mapdl_geometry_rack import RackProfile
from mapdl_geometry_angle import AngleProfile
from mapdl_geometry_plate import PlateProfile
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
        self.materialList = materialList
        self.material = Material(self.mapdl)

        for i, material in enumerate(self.materialList):
            self.material.createMaterial(i + 1, material["materialType"], material["materialProperties"])
    
    def createFiniteElement(self):
        self.finiteElement = FiniteElement()
        self.finiteElement.createShell181(self.mapdl)
    
    def createProfile(self, profileProps):
        self.sectionType = profileProps[0]
        if self.sectionType["I"]:
            self.Iprofile = IProfile(self.mapdl, profileProps[1])
            self.Iprofile.createSection()
            self.Iprofile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["tubular"]:
            self.tubularProfile = TubularProfile(self.mapdl, profileProps[1])
            self.tubularProfile.createSection()
            self.tubularProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["C"]:
            self.CProfile = CProfile(self.mapdl, profileProps[1])
            self.CProfile.createSection()
            self.CProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["C2"]:
            self.C2Profile = C2Profile(self.mapdl, profileProps[1])
            self.C2Profile.createSection()
            self.C2Profile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["rack"]:
            self.RackProfile = RackProfile(self.mapdl, profileProps[1])
            self.RackProfile.createSection()
            self.RackProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["angle"]:
            self.AngleProfile = AngleProfile(self.mapdl, profileProps[1])
            self.AngleProfile.createSection()
            self.AngleProfile.createProfile(profileProps[2], profileProps[3])
        
        elif self.sectionType["plate"]:
            self.PlateProfile = PlateProfile(self.mapdl, profileProps[1])
            self.PlateProfile.createSection()
            self.PlateProfile.createProfile(profileProps[2], profileProps[3])
    
    def setMaterial(self):
        if self.sectionType["I"]:
            self.Iprofile.setMaterial()

        elif self.sectionType["tubular"]:
            self.tubularProfile.setMaterial()

        elif self.sectionType["C"]:
            self.CProfile.setMaterial()

        elif self.sectionType["C2"]:
            self.C2Profile.setMaterial()

        elif self.sectionType["rack"]:
            self.RackProfile.setMaterial()

        elif self.sectionType["angle"]:
            self.AngleProfile.setMaterial()
        
        elif self.sectionType["plate"]:
            self.PlateProfile.setMaterial()

    def createMesh(self, meshData):
        self.mapdl.mshkey(meshData["method"])
        self.mapdl.mshape(meshData["type"])
        self.mapdl.aesize("ALL", meshData["elementSize"])
        self.mapdl.asel("ALL")
        self.mapdl.amesh("ALL")
        self.mapdl.seltol(meshData["elementSize"]/2)
        # self.mapdl.finish()

    def setBoundaryConditions(self, boundaryConditions):
        self.mapdl.run("/SOLU")
        if self.sectionType["I"]:
            self.Iprofile.setBoundaryConditions(boundaryConditions)

        elif self.sectionType["tubular"]:
            self.tubularProfile.setBoundaryConditions(boundaryConditions)

        elif self.sectionType["C"]:
            self.CProfile.setBoundaryConditions(boundaryConditions)

        elif self.sectionType["C2"]:
            self.C2Profile.setBoundaryConditions(boundaryConditions)

        elif self.sectionType["rack"]:
            self.RackProfile.setBoundaryConditions(boundaryConditions)

        elif self.sectionType["angle"]:
            self.AngleProfile.setBoundaryConditions(boundaryConditions)
        
        elif self.sectionType["plate"]:
            self.PlateProfile.setBoundaryConditions(boundaryConditions)

    def open_gui(self):
        self.mapdl.open_gui()
