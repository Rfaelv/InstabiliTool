from ansys.mapdl.core import launch_mapdl
from mapdl_material import Material
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

    def setMaterialProperties(self, materialID, materialType, materialProperties):
        self.material = Material(self.mapdl)
        self.material.setMaterialProperties(materialID, materialType, materialProperties)