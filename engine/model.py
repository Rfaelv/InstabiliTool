import json


class Model():
    def __init__(self, pathToModel):
        self.pathToModel = pathToModel

        # with open(self.pathToModel, 'r') as jfile:
	    #     self.model = json.load(jfile)
        self.model = {"analysiType":{"linear":True,"nonlinear":False},"materials":[{"tag":"mat1","materialType":{"isotropic":True,"orthotropic":False,"anisotropic":False},"materialProperties":{"E":20000,"v":0.3,"dens":1800}}],"sectionType":{"I":True,"tubular":False,"C":False,"C2":False,"rack":False,"angle":False,"plate":False},"sectionProperties":{"d":0.3,"bfs":0.3,"bfi":0.3,"tw":0.01,"tfs":0.01,"tfi":0.01,"L":4,"materialAssignment":[1,1,1]},"meshType":{"rectangle":True,"triangle":False},"meshProperties":{"elementSize":0.01,"method":1},"boundaryConditions":{"1":{"UX":True,"UY":True,"UZ":True,"ROTX":False,"ROTY":False,"ROTZ":True},"2":{"UX":False,"UY":False,"UZ":False,"ROTX":False,"ROTY":False,"ROTZ":False},"3":{"UX":True,"UY":True,"UZ":True,"ROTX":False,"ROTY":False,"ROTZ":True},"personalized":True,"table":[["Coordinates",'none','none',"Restrinctions",'none','none','none','none','none'],["X","Y","Z","UX","UY","UZ","ROTX","ROTY","ROTZ"],[0.15,0.29,1,"fixed","free","free","free","free","free"],[-0.15,0.29,1,"fixed","free","free","free","free","free"],[0.15,0,1,"fixed","free","free","free","free","free"],[-0.15,0,1,"fixed","free","free","free","free","free"],[0.15,0.29,3,"fixed","free","free","free","free","free"],[-0.15,0.29,3,"fixed","free","free","free","free","free"],[0.15,0,3,"fixed","free","free","free","free","free"],[-0.15,0,3,"fixed","free","free","free","free","free"]]},"loadType":{"bending":True,"normal":False},"loadProperties":{"points":4,"Lshear":1}}
    
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
        return self.model['boundaryConditions']

    def load(self):
        return