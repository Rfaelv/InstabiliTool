class Material:
    def __init__(self, mapdl):
        self.mapdl = mapdl
        self.mapdl.run("/PREP7")

    def setMaterialProperties(self, materialID, materialType, materialProperties):
        self.id = materialID
        self.materialType = materialType
        self.materialProperties = materialProperties

        if self.materialType["isotropic"]:
            self.mapdl.mp("EX", self.id, self.materialProperties["E"])
            self.mapdl.mp("PRXY", self.id, self.materialProperties["v"])
            self.mapdl.mp("DENS", self.id, self.materialProperties["dens"])

        elif self.materialType["orthotropic"]:
            self.mapdl.mp("EX", self.id, self.materialProperties["Ex"])
            self.mapdl.mp("EY", self.id, self.materialProperties["Ey"])
            self.mapdl.mp("EZ", self.id, self.materialProperties["Ez"])
            self.mapdl.mp("PRXY", self.id, self.materialProperties["vxy"])
            self.mapdl.mp("PRYZ", self.id, self.materialProperties["vyz"])
            self.mapdl.mp("PRXZ", self.id, self.materialProperties["vxz"])
            self.mapdl.mp("GXY", self.id, self.materialProperties["Gxy"])
            self.mapdl.mp("GYZ", self.id, self.materialProperties["Gyz"])
            self.mapdl.mp("GXZ", self.id, self.materialProperties["Gxz"])
            self.mapdl.mp("DENS", self.id, self.materialProperties["dens"])

        elif self.materialType["anisotropic"]:
            import numpy as np 
            K = np.array(self.materialProperties["stiffnessMatrix"])
            K = K.reshape(6, 6)

            self.mapdl.run(f"TB,anel, {self.id},,,0") # the last input: 0 - stiffness matrix, 1 - flexibility matrix
            self.mapdl.tbdata(1, K[0,0], K[0,1], K[0,2], K[0,3], K[0,4], K[0,5])
            self.mapdl.tbdata(7, K[1,1], K[1,2], K[1,3], K[1,4], K[1,5], K[2,2])
            self.mapdl.tbdata(13, K[2,3], K[2,4], K[2,5], K[3,3], K[3,4], K[3,5])
            self.mapdl.tbdata(19, K[4,4], K[4,5], K[5,5])

            self.mapdl.mp("DENS", self.id, self.materialProperties["dens"])

    def getMaterialProperties(self):
        return
