class MaterialProperties:
    def __init__(self, mapdl, id):
        self.mapdl = mapdl
        self.id = id
        self.mapdl.run("/PREP7")

    def setMaterialProperties(self, materialType, materialProperties):
        self.materialType = materialType
        self.materialProperties = materialProperties

        if self.materialType["isotropic"]:
            self.mapdl.mp("EX", self.id, self.materialProperties["EX"])
            self.mapdl.mp("PRXY", self.id, self.materialProperties["PRXY"])
            self.mapdl.mp("DENS", self.id, self.materialProperties["DENS"])

        elif self.materialType["orthotropic"]:
            self.mapdl.mp("EX", self.id, self.materialProperties["EX"])
            self.mapdl.mp("EY", self.id, self.materialProperties["EY"])
            self.mapdl.mp("EZ", self.id, self.materialProperties["EZ"])
            self.mapdl.mp("PRXY", self.id, self.materialProperties["PRXY"])
            self.mapdl.mp("PRYZ", self.id, self.materialProperties["PRYZ"])
            self.mapdl.mp("PRXZ", self.id, self.materialProperties["PRXZ"])
            self.mapdl.mp("GXY", self.id, self.materialProperties["GXY"])
            self.mapdl.mp("GYZ", self.id, self.materialProperties["GYZ"])
            self.mapdl.mp("GXZ", self.id, self.materialProperties["GZ"])
            self.mapdl.mp("DENS", self.id, self.materialProperties["DENS"])

        elif self.materialType.anisotropic:
            for i, row in self.materialProperties:
                for j, value in enumerate(row):
                    self.mapdl.mp(f"D{i}{j}", self.id, value)
    
    def getMaterialProperties(self):
        return self.props
