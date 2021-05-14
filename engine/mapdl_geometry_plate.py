class PlateProfile:
    def __init__(self, mapdl, sectionProps):
        self.mapdl = mapdl
        self.d = sectionProps['d']
        self.t = sectionProps['t']
        self.L = sectionProps['L']
        self.bw = self.d

        self.materialAssignment = sectionProps["materialAssignment"]

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, 1)
        
    def createProfile(self, loadType, loadProps):
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.L/2)
                self.mapdl.k(102, 0, self.bw, self.L/2)

                self.mapdl.k(201, 0, 0, self.L)
                self.mapdl.k(202, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)

                self.mapdl.a(101, 102, 202, 201)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.Lshear)
                self.mapdl.k(102, 0, self.bw, self.Lshear)

                self.mapdl.k(201, 0, 0, self.L - self.Lshear)
                self.mapdl.k(202, 0, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, 0, 0, self.L)
                self.mapdl.k(302, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)

                self.mapdl.a(101, 102, 202, 201)

                self.mapdl.a(201, 202, 302, 301)

        else:
            self.mapdl.k(1, 0, 0, 0)
            self.mapdl.k(2, 0, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, 0, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)

    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.aatt(self.materialAssignment[0], 1, 1, 0, 1) 
