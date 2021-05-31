class TubularProfile:
    def __init__(self, mapdl, sectionProps):
        self.mapdl = mapdl
        self.d = sectionProps['d']
        self.b = sectionProps['b']
        self.t = sectionProps['t']
        self.L = sectionProps['L']
        self.bw = self.d - self.t
        self.bf = self.b - self.t

        self.materialAssignment = sectionProps["materialAssignment"]

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "flange")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[0])
        self.mapdl.sectype(2, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[1])

    def createProfile(self, loadType, loadProps):
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, self.bf, self.bw, 0)
                self.mapdl.k(4, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.L/2)
                self.mapdl.k(102, self.bf, 0, self.L/2)
                self.mapdl.k(103, self.bf, self.bw, self.L/2)
                self.mapdl.k(104, 0, self.bw, self.L/2)

                self.mapdl.k(201, 0, 0, self.L)
                self.mapdl.k(202, self.bf, self.bw, self.L)
                self.mapdl.k(203, self.bf, 0, self.L)
                self.mapdl.k(204, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(4, 1, 101, 104)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(104, 101, 201, 204)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, self.bf, self.bw, 0)
                self.mapdl.k(4, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.Lshear)
                self.mapdl.k(102, self.bf, 0, self.Lshear)
                self.mapdl.k(103, self.bf, self.bw, self.Lshear)
                self.mapdl.k(104, 0, self.bw, self.Lshear)

                self.mapdl.k(201, 0, 0, self.L - self.Lshear)
                self.mapdl.k(202, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(203, self.bf, self.bw, self.L - self.Lshear)
                self.mapdl.k(204, 0, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, 0, 0, self.L)
                self.mapdl.k(302, self.bf, 0, self.L)
                self.mapdl.k(303, self.bf, self.bw, self.L)
                self.mapdl.k(304, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(4, 1, 101, 104)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(104, 101, 201, 204)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(202, 203, 303, 302)
                self.mapdl.a(203, 204, 304, 303)
                self.mapdl.a(204, 201, 301, 304)
        else:
            self.mapdl.k(1, 0, 0, 0)
            self.mapdl.k(2, self.bf, 0, 0)
            self.mapdl.k(3, self.bf, self.bw, 0)
            self.mapdl.k(4, 0, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, self.bf, 0, self.L)
            self.mapdl.k(103, self.bf, self.bw, self.L)
            self.mapdl.k(104, 0, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(2, 3, 103, 102)
            self.mapdl.a(3, 4, 104, 103)
            self.mapdl.a(4, 1, 101, 104)

    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", 0)
        self.mapdl.asel("A", "LOC", "Y", self.bw)
        self.mapdl.aatt(self.materialAssignment[0], 1, 1, 0, 1) 

        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "X", 0)
        self.mapdl.asel("A", "LOC", "X", self.bf)
        self.mapdl.aatt(self.materialAssignment[1], 2, 1, 0, 2)

    def setBoundaryConditions(self, boundaryConditions):
        if boundaryConditions['personalized']:
            bc2 = boundaryConditions['2']
            self.mapdl.nsel("S", "LOC", "X", 0)
            self.mapdl.nsel("R", "LOC", "Z", 0)
            for key in bc2:
                if bc2[key]:
                    self.mapdl.d('ALL', key, 0)
            
            self.mapdl.nsel("S", "LOC", "X", self.bf)
            self.mapdl.nsel("R", "LOC", "Z", 0)
            for key in bc2:
                if bc2[key]:
                    self.mapdl.d('ALL', key, 0)

            self.mapdl.nsel("S", "LOC", "X", 0)
            self.mapdl.nsel("R", "LOC", "Z", self.L)
            for key in bc2:
                if bc2[key]  and key != 'UZ':
                    self.mapdl.d('ALL', key, 0)
            
            self.mapdl.nsel("S", "LOC", "X", self.bf)
            self.mapdl.nsel("R", "LOC", "Z", self.L)
            for key in bc2:
                if bc2[key]  and key != 'UZ':
                    self.mapdl.d('ALL', key, 0)

            bc1 = boundaryConditions['1']
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("R", "LOC", "Y", 0)
            for key in bc1:
                if bc1[key]:
                    self.mapdl.d('ALL', key, 0)
            
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("R", "LOC", "Y", self.bw)
            for key in bc1:
                if bc1[key]:
                    self.mapdl.d('ALL', key, 0)

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.nsel("R", "LOC", "Y", 0)
            for key in bc1:
                if bc1[key] and key != 'UZ':
                    self.mapdl.d('ALL', key, 0)
            
            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.nsel("R", "LOC", "Y", self.bw)
            for key in bc1:
                if bc1[key] and key != 'UZ':
                    self.mapdl.d('ALL', key, 0)
            
            if boundaryConditions['table'] != '':
                for i, row in enumerate(boundaryConditions['table']):
                    if i not in [0, 1]:
                        self.mapdl.nsel('S', 'LOC', 'X', row[0])
                        self.mapdl.nsel('R', 'LOC', 'Y', row[1])
                        self.mapdl.nsel('R', 'LOC', 'Z', row[2])
                        for j in range(6):
                            if row[3 + j] in ['fixed', 'fixo']:
                                self.mapdl.d('ALL', boundaryConditions['table'][1][3 + j], 0)

        else:
            if boundaryConditions['S-S']:
                self.mapdl.nsel("S", "LOC", "Z", 0)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
                self.mapdl.d("ALL", "UZ", 0)
                self.mapdl.nsel("S", "LOC", "Z", self.L)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)

            elif boundaryConditions['C-F']:
                self.mapdl.nsel("S", "LOC", "Z", 0)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
                self.mapdl.d("ALL", "UZ", 0)
                self.mapdl.d("ALL", "ROTX", 0)
                self.mapdl.d("ALL", "ROTY", 0)
                self.mapdl.d("ALL", "ROTZ", 0)

            elif boundaryConditions['C-C']:
                self.mapdl.nsel("S", "LOC", "Z", 0)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
                self.mapdl.d("ALL", "UZ", 0)
                self.mapdl.d("ALL", "ROTX", 0)
                self.mapdl.d("ALL", "ROTY", 0)
                self.mapdl.d("ALL", "ROTZ", 0)
                self.mapdl.nsel("S", "LOC", "Z", self.L)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
                self.mapdl.d("ALL", "ROTX", 0)
                self.mapdl.d("ALL", "ROTY", 0)
                self.mapdl.d("ALL", "ROTZ", 0)

            elif boundaryConditions['C-S']:
                self.mapdl.nsel("S", "LOC", "Z", 0)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
                self.mapdl.d("ALL", "UZ", 0)
                self.mapdl.d("ALL", "ROTX", 0)
                self.mapdl.d("ALL", "ROTY", 0)
                self.mapdl.d("ALL", "ROTZ", 0)
                self.mapdl.nsel("S", "LOC", "Z", self.L)
                self.mapdl.d("ALL", "UX", 0)
                self.mapdl.d("ALL", "UY", 0)
    
    def setBendingLoad(self, bendingLoadProperties):
        if bendingLoadProperties["points"] == 4:
            self.mapdl.fk(103, "FY", -0.5)
            self.mapdl.fk(104, "FY", -0.5)
            self.mapdl.fk(203, "FY", -0.5)
            self.mapdl.fk(204, "FY", -0.5)
        elif bendingLoadProperties["points"] == 3:
            self.mapdl.fk(103, "FY", -0.5)
            self.mapdl.fk(104, "FY", -0.5)
    
    def setNormalLoad(self, normalLoadProperties):
        return