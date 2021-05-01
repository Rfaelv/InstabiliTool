from mapdl_initialize import MapdlInitialize
from mpdl_materialProperties import MaterialProperties


mapdl = MapdlInitialize().getInstance()

mat1 = MaterialProperties(mapdl, 1)
mat1.setMaterialProperties({"isotropic": True}, {"EX": 20000, "PRXY": 0.3, "DENS": 1900})

mapdl.open_gui()