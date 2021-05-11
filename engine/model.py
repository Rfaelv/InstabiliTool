import json


class Model():
    def __init__(self, pathToModel):
        self.pathToModel = pathToModel

        # with open(self.pathToModel, 'r') as jfile:
	    #     self.model = json.load(jfile)
        self.model = {"analysiType":{"linear":True,"nonlinear":False},"materials":[{"tag":"mate1","materialType":{"isotropic":True,"orthotropic":False,"anisotropic":False},"materialProperties":{"E":2000000,"v":0.3,"dens":1600}},{"tag":"mate2","materialType":{"isotropic":False,"orthotropic":True,"anisotropic":False},"materialProperties":{"Ex":3000000,"Ey":3000000,"Ez":2500000,"vxy":0.3,"vyz":0.16,"vxz":0.16,"Gxy":2500000,"Gyz":2500000,"Gxz":2500000,"dens":1900}}],"sectionType":{"I":True,"tubular":False,"C":False,"C2":False,"rack":False,"angle":False},"sectionProperties":{"d":0.3,"bfs":0.2,"bfi":0.1,"tw":0.01,"tfs":0.01,"tfi":0.01,"L":4},"meshType":{"rectangle":True,"triangle":False},"meshProperties":{},"boundaryConditions":{},"loadType":{"bending":True,"normal":False},"loadProperties":{"points":4,"Lshear":1.5}}
    
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
        return

    def boundaryConditions(self):
        return

    def load(self):
        return