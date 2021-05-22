from mapdl import Mapdl
from model import Model

# BACKBONE

mapdl = Mapdl('path-to-launch-mapdl')
model = Model('path-to-model.json')
mapdl.initialize()
mapdl.createProfile(model.section())
mapdl.createMesh(model.mesh())
mapdl.saveMeshImage()
