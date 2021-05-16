import json


class Model():
    def __init__(self, pathToModel):
        self.pathToModel = pathToModel

        # with open(self.pathToModel, 'r') as jfile:
	    #     self.model = json.load(jfile)
        self.model = {"analysiType":{"linear":True,"nonlinear":False},"materials":[{"tag":"mfh","materialType":{"isotropic":True,"orthotropic":False,"anisotropic":False},"materialProperties":{"E":565,"v":0.3,"dens":8}},{"tag":"45","materialType":{"isotropic":True,"orthotropic":False,"anisotropic":False},"materialProperties":{"E":87,"v":0.3,"dens":45}},{"tag":"3","materialType":{"isotropic":True,"orthotropic":False,"anisotropic":False},"materialProperties":{"E":525252,"v":0.3,"dens":52222}}],"sectionType":{"I":False,"tubular":False,"C":False,"C2":False,"rack":True,"angle":False},"sectionProperties":{"d":0.3,"b":0.2,"bfi":0.2,"t":0.01,"z":0.1,"zi":0.1,"y":0.1,"yi":0.1,"L":3,"materialAssignment":[1,2,3]},"meshType":{"rectangle":True,"triangle":False},"meshProperties":{"elementSize":0.01,"method":0},"boundaryConditions":{},"loadType":{"bending":True,"normal":False},"loadProperties":{"points":3}}
    
    def analysiType(self):
        return

    def materialList(self):
        return self.model["materials"]

    def section(self):
        return [self.model["sectionType"],
                self.model["sectionProperties"],
                self.model["loadType"],
                self.model["loadProperties"]]

    def mesh(self):
        return self.model["meshProperties"]

    def boundaryConditions(self):
        return

    def load(self):
        return