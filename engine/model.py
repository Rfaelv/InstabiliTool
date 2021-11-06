import json


class Model():
    def __init__(self, pathToModel):

        with open(pathToModel, 'r') as jfile:
	        self.model = json.load(jfile)
    
        self.analysisType = self.model["analysiType"]
        self.materialList = self.model["materials"]
        self.section = [self.model["sectionType"],
                        self.model["sectionProperties"],
                        self.model["loadType"],
                        self.model["loadProperties"]]
        self.mesh = self.model["meshProperties"]
        self.boundaryConditions = self.model['boundaryConditions']
        self.load = [self.model["loadType"],
                     self.model["loadProperties"]]