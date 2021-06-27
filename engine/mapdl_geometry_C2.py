class C2Profile:
    def __init__(self, mapdl, sectionProps):
        self.mapdl = mapdl
        self.d = sectionProps['d']
        self.b = sectionProps['b']
        self.t = sectionProps['t']
        self.z = sectionProps['z']
        self.L = sectionProps['L']
        self.bw = self.d - self.t
        self.bf = self.b - self.t
        self.zf = self.z - self.t / 2

        self.materialAssignment = sectionProps["materialAssignment"]

        self.xcg = (2 * (self.bf * self.t * self.bf / 2 + self.z * self.t * self.bf)) / (((self.bw - self.t) + 2 * (self.bf + self.z)) * self.t)
        self.ycg = self.bw / 2

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "flangeS")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[0])
        self.mapdl.sectype(2, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[1])
        self.mapdl.sectype(3, "SHELL", "", "flangeI")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[2])

    def createProfile(self, loadType, loadProps):
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, self.bf, self.zf, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, 0, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bf, self.bw, 0)
                self.mapdl.k(6, self.bf, self.bw - self.zf, 0)

                self.mapdl.k(101, self.bf, self.zf, self.L/2)
                self.mapdl.k(102, self.bf, 0, self.L/2)
                self.mapdl.k(103, 0, 0, self.L/2)
                self.mapdl.k(104, 0, self.bw, self.L/2)
                self.mapdl.k(105, self.bf, self.bw, self.L/2)
                self.mapdl.k(106, self.bf, self.bw - self.zf, self.L/2)

                self.mapdl.k(201, self.bf, self.zf, self.L)
                self.mapdl.k(202, self.bf, 0, self.L)
                self.mapdl.k(203, 0, 0, self.L)
                self.mapdl.k(204, 0, self.bw, self.L)
                self.mapdl.k(205, self.bf, self.bw, self.L)
                self.mapdl.k(206, self.bf, self.bw - self.zf, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(5, 6, 106, 105)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(105, 106, 206, 205)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, self.bf, self.zf, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, 0, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bf, self.bw, 0)
                self.mapdl.k(6, self.bf, self.bw - self.zf, 0)

                self.mapdl.k(101, self.bf, self.zf, self.Lshear)
                self.mapdl.k(102, self.bf, 0, self.Lshear)
                self.mapdl.k(103, 0, 0, self.Lshear)
                self.mapdl.k(104, 0, self.bw, self.Lshear)
                self.mapdl.k(105, self.bf, self.bw, self.Lshear)
                self.mapdl.k(106, self.bf, self.bw - self.zf, self.Lshear)

                self.mapdl.k(201, self.bf, self.zf, self.L - self.Lshear)
                self.mapdl.k(202, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(203, 0, 0, self.L - self.Lshear)
                self.mapdl.k(204, 0, self.bw, self.L - self.Lshear)
                self.mapdl.k(205, self.bf, self.bw, self.L - self.Lshear)
                self.mapdl.k(206, self.bf, self.bw - self.zf, self.L - self.Lshear)

                self.mapdl.k(301, self.bf, self.zf, self.L)
                self.mapdl.k(302, self.bf, 0, self.L)
                self.mapdl.k(303, 0, 0, self.L)
                self.mapdl.k(304, 0, self.bw, self.L)
                self.mapdl.k(305, self.bf, self.bw, self.L)
                self.mapdl.k(306, self.bf, self.bw - self.zf, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(5, 6, 106, 105)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(102, 103, 203, 202)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(105, 106, 206, 205)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(202, 203, 303, 302)
                self.mapdl.a(203, 204, 304, 303)
                self.mapdl.a(204, 205, 305, 304)
                self.mapdl.a(205, 206, 306, 305)

        else:
            self.mapdl.k(1, self.bf, self.zf, 0)
            self.mapdl.k(2, self.bf, 0, 0)
            self.mapdl.k(3, 0, 0, 0)
            self.mapdl.k(4, 0, self.bw, 0)
            self.mapdl.k(5, self.bf, self.bw, 0)
            self.mapdl.k(6, self.bf, self.bw - self.zf, 0)

            self.mapdl.k(101, self.bf, self.zf, self.L)
            self.mapdl.k(102, self.bf, 0, self.L)
            self.mapdl.k(103, 0, 0, self.L)
            self.mapdl.k(104, 0, self.bw, self.L)
            self.mapdl.k(105, self.bf, self.bw, self.L)
            self.mapdl.k(106, self.bf, self.bw - self.zf, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(2, 3, 103, 102)
            self.mapdl.a(3, 4, 104, 103)
            self.mapdl.a(4, 5, 105, 104)
            self.mapdl.a(5, 6, 106, 105)

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

    def setBoundaryConditions(self, boundaryConditions):
        if boundaryConditions['personalized']:
            for item in boundaryConditions["data"]:
                bc2 = item['2']
                self.mapdl.nsel("S", "LOC", "X", 0)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc2:
                    if bc2[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)

                bc1 = item['1']
                self.mapdl.nsel("S", "LOC", "Y", self.bw/2, self.bw)
                self.mapdl.nsel("U", "LOC", "X", 0)
                self.mapdl.nsel("A", "LOC", "Y", self.bw)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc1:
                    if bc1[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)

                bc3 = item['3']
                self.mapdl.nsel("S", "LOC", "Y", 0, self.bw/2)
                self.mapdl.nsel("U", "LOC", "X", 0)
                self.mapdl.nsel("A", "LOC", "Y", 0)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc3:
                    if bc3[key] and key != "all":
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
            self.mapdl.fk(104, "FY", -1)
            self.mapdl.fk(204, "FY", -1)

        elif bendingLoadProperties["points"] == 3:
            self.mapdl.fk(104, "FY", -1)
    
    def setNormalLoad(self, normalLoadProperties):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/(2 * (self.bf + self.zf) + self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", - 1/(2 * (self.bf + self.zf) + self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.k(7, self.xcg, self.ycg, 0)
            self.mapdl.k(107, self.xcg, self.ycg, self.L)

            self.mapdl.a(107,101,102,103,104,105,106)
            self.mapdl.a(107,101,106)

            self.mapdl.a(7,1,2,3,4,5,6)
            self.mapdl.a(7,1,6)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.01)
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")
            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.run("/SOLU")

            self.mapdl.fk(107, "FZ", -1)
            self.mapdl.fk(107, "MX", ex)
            self.mapdl.fk(107, "MY", ey)
            self.mapdl.fk(7, "FZ", 1)
            self.mapdl.fk(7, "MX", - ex)
            self.mapdl.fk(7, "MY", - ey)