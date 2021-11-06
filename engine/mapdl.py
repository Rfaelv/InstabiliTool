from ansys.mapdl.core import launch_mapdl
from numpy.lib import financial
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
            self.mapdl = launch_mapdl(exec_file=self.settings.execFilePath, run_location=self.pathToLaunch, override=True, start_instance=False, clear_on_connect=True, loglevel='WARNING', cleanup_on_exit=True)
        except OSError:
            try:
                self.mapdl = launch_mapdl(exec_file=self.settings.execFilePath, run_location=self.pathToLaunch, override=True,  loglevel='WARNING', cleanup_on_exit=True) 
            except:
                print('ERROR-launch_mapdl')
                sys.exit()
                
    def getInstance(self):
        return self.mapdl

    def createFiniteElement(self):
        self.finiteElement = FiniteElement(self.mapdl)
        self.finiteElement.createShell181(self.settings["general"])

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
            self.tubularProfile = TubularProfile(self.mapdl, profileProps[1], self.settings)
            self.tubularProfile.createSection()
            self.tubularProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["C"]:
            self.CProfile = CProfile(self.mapdl, profileProps[1], self.settings)
            self.CProfile.createSection()
            self.CProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["C2"]:
            self.C2Profile = C2Profile(self.mapdl, profileProps[1], self.settings)
            self.C2Profile.createSection()
            self.C2Profile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["rack"]:
            self.RackProfile = RackProfile(self.mapdl, profileProps[1], self.settings)
            self.RackProfile.createSection()
            self.RackProfile.createProfile(profileProps[2], profileProps[3])

        elif self.sectionType["angle"]:
            self.AngleProfile = AngleProfile(self.mapdl, profileProps[1], self.settings)
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

    def runStaticAnalysis(self):
        self.mapdl.antype("STATIC")
        self.mapdl.pstres("ON")
        self.mapdl.allsel("ALL")
        self.mapdl.solve()
        self.mapdl.finish()

    def runBucklingAnalysis(self, analysiType):
        self.analysisType = analysiType

        def setNewLoad(newLoad):
            if self.loadType["bending"]:
                if self.sectionType["I"]:
                    self.Iprofile.setNewBendingLoad(self.loadProperties, newLoad)

                elif self.sectionType["tubular"]:
                    self.tubularProfile.setNewBendingLoad(self.loadProperties, newLoad)

                elif self.sectionType["C"]:
                    self.CProfile.setNewBendingLoad(self.loadProperties, newLoad)

                elif self.sectionType["C2"]:
                    self.C2Profile.setNewBendingLoad(self.loadProperties, newLoad)

                elif self.sectionType["rack"]:
                    self.RackProfile.setNewBendingLoad(self.loadProperties, newLoad)

                elif self.sectionType["angle"]:
                    self.AngleProfile.setNewBendingLoad(self.loadProperties, newLoad)
                
                elif self.sectionType["plate"]:
                    self.PlateProfile.setNewBendingLoad(self.loadProperties, newLoad)

            elif self.loadType["normal"]:
                if self.sectionType["I"]:
                    self.Iprofile.setNewNormalLoad(self.loadProperties, newLoad)

                elif self.sectionType["tubular"]:
                    self.tubularProfile.setNewNormalLoad(self.loadProperties, newLoad)

                elif self.sectionType["C"]:
                    self.CProfile.setNewNormalLoad(self.loadProperties, newLoad)

                elif self.sectionType["C2"]:
                    self.C2Profile.setNewNormalLoad(self.loadProperties, newLoad)

                elif self.sectionType["rack"]:
                    self.RackProfile.setNewNormalLoad(self.loadProperties, newLoad)

                elif self.sectionType["angle"]:
                    self.AngleProfile.setNewNormalLoad(self.loadProperties, newLoad)
                
                elif self.sectionType["plate"]:
                    self.PlateProfile.setNewNormalLoad(self.loadProperties, newLoad)

        self.mapdl.run("/SOLU")
        self.mapdl.antype("BUCKLE")
        self.mapdl.bucopt("LANB", self.settings["linearAnalysis"]["nmodes"],"","","RANGE")
        self.mapdl.solve()
        self.mapdl.finish()
        self.mapdl.run("/SOLU")
        self.mapdl.expass("ON")
        self.mapdl.mxpand(self.settings["linearAnalysis"]["nmodes"])
        self.mapdl.solve()
        self.mapdl.finish()

        if self.analysisType['nonlinear']:
            loadFactor = self.settings["nonlinearAnalysis"]["loadFactor"]
            deformationFactor = self.settings["nonlinearAnalysis"]["initialDeformationFactor"]
            steps = self.settings["nonlinearAnalysis"]["steps"]

            try:
                t = self.sectionProperties["t"]
            except:
                tfs = self.sectionProperties["tfs"]
                tw = self.sectionProperties["tw"]
                tfi = self.sectionProperties["tfi"]
                t = (tfs + tw + tfi) / 2
            finally:
                imperfection = deformationFactor * t

            result = self.mapdl.result 
            firstEingenValue = result.solution_info(0)["timfrq"]

            self.mapdl.post1()
            self.mapdl.set(1, 0)
            dispLinear = self.mapdl.post_processing.nodal_displacement('NORM')

            maxDisp = np.amax(dispLinear)    

            self.mapdl.prep7()

            self.mapdl.upgeom(imperfection/maxDisp, 1, 0, 'Profile', 'rst')
            self.mapdl.allsel('all')
            self.mapdl.cdwrite('db', 'Profile', 'cdb')
            self.mapdl.finish()

            self.mapdl.post1()
            self.mapdl.pldisp(0)

            self.mapdl.run('/SOLU')

            self.mapdl.prep7()
            self.LOAD = firstEingenValue * loadFactor

            setNewLoad(self.LOAD)
            self.mapdl.finish()

            self.mapdl.run('/SOLU')
            self.mapdl.antype('static')
            self.mapdl.nlgeom('on')
            self.mapdl.pred('off')
            self.mapdl.time(1)
            nsteps = steps 
            self.mapdl.nsubst(nsteps,10000,nsteps)
            self.mapdl.rescontrol('define','all',1)
            self.mapdl.outres('all','all')
            self.mapdl.solve()
            self.mapdl.finish()
            self.mapdl.run('/file,Profile')

    def getResults(self, path):
        if self.analysisType['linear']:
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
                    L = self.sectionProperties["L"]
                    cpos = [(L, 0.6*L, 0.7*L + L),
                    (0.0, 0.0, L/2),
                    (0.0, 1, 0.0)]

                    imgPath = path + f'\\movie{i}.gif'

                    result.animate_nodal_solution(i, movie_filename=imgPath, cpos=cpos, loop=False, displacement_factor=2,  off_screen=True, progress_bar=False, add_text=False, background='w', below_color=[256,256,256],show_scalar_bar=False)
                
                except Exception:
                    continue

            return resultList
        
        else:
            nsets = self.mapdl.post_processing.nsets
            self.mapdl.post1()
            self.mapdl.set(1, nsets)

            resultsCongif = [{
                "type": "displacement",
                "direction": "Y",
                "coords": [0,0,0]
            },
            {
                "type": "strain",
                "direction": "Y",
                "coords": "max"
            }
            ]
            nodesList = []
            nodesResults = []
            self.mapdl.run('/SOLU')
            time = np.array(np.zeros(nsets))

            for item, i in enumerate(resultsCongif):
                if item["type"] == "displacement" and item["coords"] == "max":
                    disp = self.mapdl.post_processing.nodal_displacement(item["direction"])
                    dispmx = np.amax(disp)
                    nodesList.append(np.whwre(np.isclose(disp, dispmx)))

                elif item["type"] == "strain" and item["coords"] == "max":
                    disp = self.mapdl.post_processing.nodal_total_component_strain(item["direction"])
                    dispmx = np.amax(disp)
                    nodesList.append(np.whwre(np.isclose(disp, dispmx)))

                elif item["type"] == "displacement" or item["type"] == "strain":  
                    self.mapdl.nsel("S", "LOC", "X", item["coords"][0])
                    self.mapdl.nsel("R", "LOC", "Y", item["coords"][1])
                    self.mapdl.nsel("R", "LOC", "Z", item["coords"][2])
                    self.mapdl.get(f'node{i}', 'NODE', 0, 'NUM', 'MAX')
                    nodesList.append(int(self.mapdl.parameters[f'node{i}']))
                
                nodesResults.append(np.array(np.zeros(nsets)))

            self.mapdl.post1()

            for i in range(nsets):
                self.mapdl.set(1, i + 1)

                for node, j in enumerate(nodesResults):
                    if resultsCongif[j]["type"] == "displacement":
                        node[i] = self.mapdl.post_processing.nodal_displacement(resultsCongif[j]["direction"])[i]

                    elif resultsCongif[j]["type"] == "strain":
                        node[i] = self.mapdl.post_processing.nodal_total_component_strain(resultsCongif[j]["direction"])[i]

                time[i] = self.mapdl.post_processing.time
            
            if self.loadType['bending'] and 'points' in self.loadProperties:
                if self.loadProperties['points'] == 3:
                    load = time * self.LOAD * self.sectionProperties["L"] / 4
                else:
                    load = time * self.LOAD * self.sectionProperties["Lshear"]

            else:
                load = time * self.LOAD
            
            # Generate Graph
            # for 

    def open_gui(self):
        self.mapdl.open_gui()

    def exit(self):
        self.mapdl.exit()
