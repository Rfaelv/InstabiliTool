from types import MappingProxyType
from mapdl import Mapdl
from model import Model
import sys
import json
# import pyvista
# pyvista.Report(gpu=False)

# materialList = {"tag":"teste3","materialType":{"isotropic":False,"orthotropic":False,"anisotropic":True},"materialProperties":{"stiffnessMatrix":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],"dens":"1900"}}

# mapdl = MapdlInitialize().getInstance()

# mat1 = MaterialProperties(mapdl) # ATENÇÂO - Verificar se é possível entrar com uma string
# mat1.setMaterialProperties(1, material["materialType"], material["materialProperties"])

# mapdl.open_gui()
pathToModel = 'C:\\Users\Rfael\\AppData\Roaming\\analise-de-flambagem-no-ansys\\data\\model.json'
pathToRun = 'D:\\Documentos\\Python\\PROJETOS\\GUI com Electron\\analise-de-flambagem-no-ansys\\data'
# pathToModel = sys.argv[1]
# BACKBONE

mapdl = Mapdl(pathToRun)
model = Model(pathToModel)
mapdl.initialize()
mapdl.createMaterial(model.materialList())
mapdl.createFiniteElement() # Verificar se será neecessário criar um elemento para cada material
mapdl.createProfile(model.section())
mapdl.setMaterial()
mapdl.createMesh(model.mesh())
mapdl.setBoundaryConditions(model.boundaryConditions())
mapdl.setLoad(model.load())
mapdl.open_gui()
mapdl.runStaticAnalysi()
mapdl.runLinearBucklingAnalysi()
result = mapdl.getResult()

print(json.dumps(result))

# mapdl.open_gui()
mapdl.exit()

# print(help(result))
# result.save_as_vtk(teste.vtk, rsets=0)
# print(result.text_result_table(rnum=1))

