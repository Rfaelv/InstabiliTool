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
        self.mapdl.secdata(self.t, self.materialAssignment[0])
        
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
            self.mapdl.k(2, 0, self.bw / 2, 0)
            self.mapdl.k(3, 0, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, 0, self.bw / 2, self.L)
            self.mapdl.k(103, 0, self.bw, self.L)

            self.mapdl.a(1, 2, 3, 103, 102, 101)

    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.aatt(self.materialAssignment[0], 1, 1, 0, 1) 

    def setBoundaryConditions(self, boundaryConditions):
        if boundaryConditions['personalized']:
            for item in boundaryConditions["data"]:
                bc1 = item['1']
                self.mapdl.nsel("S", "LOC", "X", 0)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc1:
                    if bc1[key] and key != "all":
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
                
                self.mapdl.nsel("S", "LOC", "Z", self.L / 2)
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
                self.mapdl.d("ALL", "ROTX", 0)
                self.mapdl.d("ALL", "ROTY", 0)
                self.mapdl.d("ALL", "ROTZ", 0)

                self.mapdl.nsel("S", "LOC", "Z", self.L / 2)
                self.mapdl.d("ALL", "UZ", 0)

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
            self.mapdl.fk(102, "FY", -1)
            self.mapdl.fk(202, "FY", -1)

        elif bendingLoadProperties["points"] == 3:
            self.mapdl.fk(102, "FY", -1)
    
    def setNormalLoad(self, normalLoadProperties):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/self.bw)

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", 1 / self.bw)

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.k(4, 0.1, 0, 0)
            self.mapdl.k(104, 0.1, 0, self.L)
            self.mapdl.k(5, -0.1, 0, 0)
            self.mapdl.k(105, -0.1, 0, self.L)
            self.mapdl.k(6, -0.1, self.bw, 0)
            self.mapdl.k(106, -0.1, self.bw, self.L)
            self.mapdl.k(7, 0.1, self.bw, 0)
            self.mapdl.k(107, 0.1, self.bw, self.L)

            self.mapdl.a(102,101,102,103,104)
            self.mapdl.a(102,101,104)

            self.mapdl.a(2,1,2,3,4)
            self.mapdl.a(2,1,4)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.01)
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")
            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.run("/SOLU")

            self.mapdl.fk(102, "FZ", -1)
            self.mapdl.fk(102, "MX", ex)
            self.mapdl.fk(102, "MY", ey)
            self.mapdl.fk(2, "FZ", 1)
            self.mapdl.fk(2, "MX", - ex)
            self.mapdl.fk(2, "MY", - ey)