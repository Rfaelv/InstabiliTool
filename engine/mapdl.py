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
import json
import sys


class Mapdl:
    def __init__(self, path):
        self.path = path
        self.pathToLaunch = self.path.runLocale

        with open(self.path.settings, 'r') as jfile:
	        self.settings = json.load(jfile)

    def initialize(self):
        try:  
            # self.mapdl = launch_mapdl(run_location=self.pathToLaunch, override=True,  cleanup_on_exit=True, start_instance=False, clear_on_connect=True, remove_temp_files=True, loglevel='INFO')
            self.mapdl = launch_mapdl(run_location=self.pathToLaunch, override=True, start_instance=False, clear_on_connect=True, loglevel='INFO', cleanup_on_exit=True)
        except OSError:
            try:
                self.mapdl = launch_mapdl(run_location=self.pathToLaunch, override=True,  loglevel='INFO', cleanup_on_exit=True) 
            except:
                print('ERROR-launch_mapdl')
                sys.exit()
                
    def getInstance(self):
        return self.mapdl

    def createFiniteElement(self):
        self.finiteElement = FiniteElement(self.mapdl)
        self.finiteElement.createShell181()

        if not self.settings["general"]["connections"]["rigid"]:
            self.finiteElement.createCombin39(self.settings["general"]["connections"]["stiffness"])

    def createMaterial(self, materialList):
        self.materialList = materialList
        self.material = Material(self.mapdl)

        for i, material in enumerate(self.materialList):
            self.material.createMaterial(i + 1, material["materialType"], material["materialProperties"])
        
        self.material.createPlateLoadMaterial()
    
    def createProfile(self, profileProps):
        self.sectionType = profileProps[0]
        self.sectionProperties = profileProps[1]
        if self.sectionType["I"]:
            self.Iprofile = IProfile(self.mapdl, profileProps[1], self.settings)
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
        self.meshData = meshData
        self.mapdl.asel("ALL")
        self.mapdl.mshkey(self.meshData["method"])
        self.mapdl.mshape(self.meshData["type"])
        self.mapdl.aesize("ALL", self.meshData["elementSize"])
        self.mapdl.amesh("ALL")
        self.mapdl.seltol(self.meshData["elementSize"]/2)
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
        
    def setConnectionsIfAreNotRigid(self):
        if self.sectionType["I"]:
            self.Iprofile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

        elif self.sectionType["tubular"]:
            self.tubularProfile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

        elif self.sectionType["C"]:
            self.CProfile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

        elif self.sectionType["C2"]:
            self.C2Profile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

        elif self.sectionType["rack"]:
            self.RackProfile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

        elif self.sectionType["angle"]:
            self.AngleProfile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])
        
        elif self.sectionType["plate"]:
            self.PlateProfile.setConnectionsIfAreNotRigid(self.meshData["elementSize"])

    def setLoad(self, loadData):
        self.loadType = loadData[0]
        self.loadProperties = loadData[1]

        if self.loadType["bending"]:
            if self.sectionType["I"]:
                self.Iprofile.setBendingLoad(self.loadProperties)

            elif self.sectionType["tubular"]:
                self.tubularProfile.setBendingLoad(self.loadProperties)

            elif self.sectionType["C"]:
                self.CProfile.setBendingLoad(self.loadProperties)

            elif self.sectionType["C2"]:
                self.C2Profile.setBendingLoad(self.loadProperties)

            elif self.sectionType["rack"]:
                self.RackProfile.setBendingLoad(self.loadProperties)

            elif self.sectionType["angle"]:
                self.AngleProfile.setBendingLoad(self.loadProperties)
            
            elif self.sectionType["plate"]:
                self.PlateProfile.setBendingLoad(self.loadProperties)

        elif self.loadType["normal"]:
            if self.sectionType["I"]:
                self.Iprofile.setNormalLoad(self.loadProperties)

            elif self.sectionType["tubular"]:
                self.tubularProfile.setNormalLoad(self.loadProperties)

            elif self.sectionType["C"]:
                self.CProfile.setNormalLoad(self.loadProperties)

            elif self.sectionType["C2"]:
                self.C2Profile.setNormalLoad(self.loadProperties)

            elif self.sectionType["rack"]:
                self.RackProfile.setNormalLoad(self.loadProperties)

            elif self.sectionType["angle"]:
                self.AngleProfile.setNormalLoad(self.loadProperties)
            
            elif self.sectionType["plate"]:
                self.PlateProfile.setNormalLoad(self.loadProperties)

    def runStaticAnalysi(self):
        self.mapdl.antype("STATIC")
        self.mapdl.pstres("ON")
        self.mapdl.allsel("ALL")
        self.mapdl.solve()
        self.mapdl.finish()

    def runLinearBucklingAnalysi(self):
        self.mapdl.run("/SOLU")
        self.mapdl.antype("BUCKLE")
        self.mapdl.bucopt("LANB", 10)
        self.mapdl.solve()
        self.mapdl.finish()
        self.mapdl.run("/SOLU")
        self.mapdl.expass("ON")
        self.mapdl.mxpand(10)
        self.mapdl.solve()
        self.mapdl.finish()

    def getLinearResult(self, path):
        result = self.mapdl.result
        resultList = []
        # print(type(result.n_results))
        for i in range(result.n_results):
            # print(f'for {i}')
            if self.loadType["bending"]:
                # print('bending')
                if self.loadProperties["points"] == 4:
                    # print('4points')
                    criticalMoment = result.solution_info(i)["timfrq"] * self.loadProperties["Lshear"]

                elif self.loadProperties["points"] == 3:
                    # print('3points')
                    criticalMoment = result.solution_info(i)["timfrq"] * self.sectionProperties["L"] / 4
                
                criticalLoad = str(round(criticalMoment, 2)) + ' N.m'

            elif self.loadType["normal"]:
                # print('normal')
                criticalLoad = str(round(result.solution_info(i)["timfrq"], 2)) + ' N'
            
            resultList.append({
                "value": criticalLoad,
            })

            try:
                cpos = [(1.8178551165619061, 1.2668720677458198, 3.6927581096403452),
                (0.0762, 0.07302500000000003, 0.9000000000000001),
                (-0.1329852358128566, 0.9386144670815737, -0.31830458564238795)]

                imgPath = path + f'\\img{i}.gif'

                result.animate_nodal_solution(i, movie_filename=imgPath, cpos=cpos, loop=False, displacement_factor=2,  off_screen=True, progress_bar=False, add_text=False, background='w', below_color=[256,256,256],show_scalar_bar=False)
            
            except Exception:
                continue

        return resultList

    def open_gui(self):
        self.mapdl.open_gui()

    def exit(self):
        self.mapdl.exit()
