from mapdl import Mapdl
from model import Model
import sys
import os


# pathToModel = sys.argv[1]
pathToRun = 'D:\\Documentos\\Python\\PROJETOS\\GUI com Electron\\analise-de-flambagem-no-ansys\\data'
pathToModel = 'C:\\Users\Rfael\\AppData\Roaming\\InstabiliTool\\data\\model.json'
sys.stdout.write('terter')
try:
    mapdl = Mapdl(pathToRun)
    model = Model(pathToModel)
    mapdl.initialize()
    mapdlinstance = mapdl.getInstance()
    mapdlinstance.run("/PREP7")
    mapdl.createFiniteElement()
    mapdl.createProfile(model.section())
    mapdl.createMesh(model.mesh())
    mapdlinstance.view(1, 1, 1, 1)
    mapdlinstance.run("/RGB,INDEX,100,100,100,0")
    mapdlinstance.run("/RGB,INDEX,80,80,80,13")
    mapdlinstance.run("/RGB,INDEX,60,60,60,14")
    mapdlinstance.run("/RGB,INDEX,0,0,0,15")
    print('finished')
    mapdlinstance.eplot(vtk=False)
    # mapdlinstance.open_gui()
    mapdlinstance.exit()
    # os.system("taskkill /im Mechanical APDL Program.exe")
    # mapdl.open_gui()
    sys.exit()
except Exception as e:
    print(e)


