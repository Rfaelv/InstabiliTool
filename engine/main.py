from types import MappingProxyType
from mapdl import Mapdl
from model import Model
from path import Path
import sys
import json
# import pyvista
# pyvista.Report(gpu=False)

# materialList = {"tag":"teste3","materialType":{"isotropic":False,"orthotropic":False,"anisotropic":True},"materialProperties":{"stiffnessMatrix":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],"dens":"1900"}}

# mapdl = MapdlInitialize().getInstance()

# mat1 = MaterialProperties(mapdl) # ATENÇÂO - Verificar se é possível entrar com uma string
# mat1.setMaterialProperties(1, material["materialType"], material["materialProperties"])

# mapdl.open_gui()
# path = 'C:\\Users\Rfael\\AppData\Roaming\\InstabiliTool\\data'
# pathToModel = 'C:\\Users\Rfael\\AppData\Roaming\\InstabiliTool\\data\\model.json'
# pathToRun = 'D:\\Documentos\\Python\\PROJETOS\\GUI com Electron\\analise-de-flambagem-no-ansys\\data'
# pathToModel = sys.argv[1]
# BACKBONE

try:
    # path = Path(sys.argv[1])
    path = Path('C:/Users/Rfael/AppData/Roaming/InstabiliTool')

    mapdl = Mapdl(path)
    model = Model(path.model)
    mapdl.initialize()
    mapdl.createFiniteElement() # Ao que tudo indica, não é necessário criar um elemento para cada material
    mapdl.createMaterial(model.materialList())
    mapdl.createProfile(model.section())
    mapdl.setMaterial()
    mapdl.createMesh(model.mesh())
    mapdl.setBoundaryConditions(model.boundaryConditions())
    mapdl.setConnectionsIfAreNotRigid()
    mapdl.setLoad(model.load())

    mapdl.open_gui()
    mapdl.exit()
    mapdl.runStaticAnalysi()
    mapdl.runLinearBucklingAnalysi()


    # mapdl.open_gui()

    result = mapdl.getLinearResult(path.images)

    print(json.dumps(result))

    # mapdl.open_gui()
    mapdl.exit()

except Exception as ex:
    mapdl.exit()
    print(ex)

# print(help(result))
# result.save_as_vtk(teste.vtk, rsets=0)
# print(result.text_result_table(rnum=1))

