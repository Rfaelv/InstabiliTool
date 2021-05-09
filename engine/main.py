from mapdl import Mapdl
from model import Model

materialList = {"tag":"teste3","materialType":{"isotropic":False,"orthotropic":False,"anisotropic":True},"materialProperties":{"stiffnessMatrix":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],"dens":"1900"}}

mapdl = MapdlInitialize().getInstance()

mat1 = MaterialProperties(mapdl) # ATENÇÂO - Verificar se é possível entrar com uma string
mat1.setMaterialProperties(1, material["materialType"], material["materialProperties"])

mapdl.open_gui()

# BACKBONE

mapdl = Mapdl('pathToLaunch')
model = Model('path-to-model-model')
mapdl.initialize()
mapdl.setMaterialProperties(model.material)
mapdl.createFiniteElement()
mapdl.createSection()
mapdl.createProfile(material.section)
mapdl.createMesh(material.mesh)
mapdl.setBoundaryConditions(material.boundaryConditions)
mapdl.setLoad(material.load)
mapdl.runStaticAnalysi()
mapdl.runLinearBuckingAnalysi()