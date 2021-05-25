from mapdl import Mapdl
from model import Model
import sys
import os


pathToModel = sys.argv[1]
# print(pathToModel)
try:
    mapdl = Mapdl('path-to-launch-mapdl')
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
    mapdlinstance.exit()
    # os.system("taskkill /im Mechanical APDL Program.exe")
    # mapdl.open_gui()
    sys.exit()
except Exception as e:
    print(e)


