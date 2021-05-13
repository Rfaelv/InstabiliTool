class CProfile:
    def __init__(self, mapdl, sectionProps):
        self.mapdl = mapdl
        self.d = sectionProps['d']
        self.b = sectionProps['b']
        self.t = sectionProps['t']
        self.L = sectionProps['L']
        self.bw = self.d - self.t
        self.bf = self.b - self.t / 2

        self.materialAssignment = sectionProps["materialAssignment"]

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "flangeS")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, 1)
        self.mapdl.sectype(2, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, 2)
        self.mapdl.sectype(3, "SHELL", "", "flangeI")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, 3)

    def createProfile(self, loadType, loadProps):
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, self.bf, 0, 0)
                self.mapdl.k(2, 0, 0, 0)
                self.mapdl.k(3, 0, self.bw, 0)
                self.mapdl.k(4, self.bf, self.bw, 0)

                self.mapdl.k(101, self.bf, 0, self.L/2)
                self.mapdl.k(102, 0, 0, self.L/2)
                self.mapdl.k(103, 0, self.bw, self.L/2)
                self.mapdl.k(104, self.bf, self.bw, self.L/2)

                self.mapdl.k(201, self.bf, 0, self.L)
                self.mapdl.k(202, 0, 0, self.L)
                self.mapdl.k(203, 0, self.bw, self.L)
                self.mapdl.k(204, self.bf, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, self.bf, 0, 0)
                self.mapdl.k(2, 0, 0, 0)
                self.mapdl.k(3, 0, self.bw, 0)
                self.mapdl.k(4, self.bf, self.bw, 0)

                self.mapdl.k(101, self.bf, 0, self.Lshear)
                self.mapdl.k(102, 0, 0, self.Lshear)
                self.mapdl.k(103, 0, self.bw, self.Lshear)
                self.mapdl.k(104, self.bf, self.bw, self.Lshear)

                self.mapdl.k(201, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(202, 0, 0, self.L - self.Lshear)
                self.mapdl.k(203, 0, self.bw, self.L - self.Lshear)
                self.mapdl.k(204, self.bf, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, self.bf, 0, self.L)
                self.mapdl.k(302, 0, 0, self.L)
                self.mapdl.k(303, 0, self.bw, self.L)
                self.mapdl.k(304, self.bf, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(202, 203, 303, 302)
                self.mapdl.a(203, 204, 304, 303)

        else:
            self.mapdl.k(1, self.bf, 0, 0)
            self.mapdl.k(2, 0, 0, 0)
            self.mapdl.k(3, 0, self.bw, 0)
            self.mapdl.k(4, self.bf, self.bw, 0)

            self.mapdl.k(101, self.bf, 0, self.L)
            self.mapdl.k(102, 0, 0, self.L)
            self.mapdl.k(103, 0, self.bw, self.L)
            self.mapdl.k(104, self.bf, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(2, 3, 103, 102)
            self.mapdl.a(3, 4, 104, 103)

    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", self.bw/2, self.bw)
        self.mapdl.aatt(self.materialAssignment[0], 1, 1, 0, 1)

        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", 0, self.bw/2)
        self.mapdl.aatt(self.materialAssignment[2], 3, 1, 0, 3)

        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "X", 0)
        self.mapdl.aatt(self.materialAssignment[1], 2, 1, 0, 2)
