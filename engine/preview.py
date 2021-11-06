from mapdl import Mapdl
from model import Model
from path import Path
import sys


# pathToModel = sys.argv[1]
# pathToLaunch = sys.argv[2]
# pathToLaunch = 'D:\\Documentos\\Python\\PROJETOS\\GUI com Electron\\analise-de-flambagem-no-ansys\\data'
# pathToModel = 'C:\\Users\Rfael\\AppData\Roaming\\InstabiliTool\\data\\model.json'

# try:
path = Path(sys.argv[1])
# path = Path('C:/Users/Rfael/AppData/Roaming/InstabiliTool')

mapdl = Mapdl(path)
model = Model(path.model)
mapdl.initialize()
mapdlinstance = mapdl.getInstance()
mapdlinstance.run("/PREP7")
mapdl.createFiniteElement()
mapdl.createProfile(model.section)
mapdl.createMesh(model.mesh)
mapdlinstance.view(1, 1, 1, 1)
mapdlinstance.run("/RGB,INDEX,100,100,100,0")
mapdlinstance.run("/RGB,INDEX,80,80,80,13")
mapdlinstance.run("/RGB,INDEX,60,60,60,14")
mapdlinstance.run("/RGB,INDEX,0,0,0,15")
mapdlinstance.eplot(vtk=False)
mapdlinstance.exit()

sys.exit()

# except Exception as e:
#     print(e)
