class AngleProfile:
    def __init__(self, mapdl, sectionProps, settings):
        self.mapdl = mapdl
        self.settings = settings
        self.d = sectionProps['d']
        self.b = sectionProps['b']
        self.t = sectionProps['t']
        self.L = sectionProps['L']
        self.bw = self.d - self.t/2
        self.bf = self.b - self.t/2

        self.materialAssignment = sectionProps["materialAssignment"]

        self.xcg = (self.b * self.t * (self.b / 2 - self.t / 2)) / ((self.bw - self.t + self.b) * self.t)
        self.ycg = self.bw / 2

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[0])
        self.mapdl.sectype(2, "SHELL", "", "flange")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.t, self.materialAssignment[1])

        self.mapdl.sectype(3, "SHELL", "", "plateLoad")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(0.1, 100)
        
    def createProfile(self, loadType, loadProps):
        self.connectionsIsNotRigid = not self.settings["general"]["connections"]["rigid"]
        if loadType['bending'] and 'points' in loadProps:
            if loadProps['points'] == 3:
                self.mapdl.k(1, self.bf, 0, 0)
                self.mapdl.k(2, 0, 0, 0)
                self.mapdl.k(3, 0, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(22, 0, 0, 0)

                self.mapdl.k(101, self.bf, 0, self.L/2)
                self.mapdl.k(102, 0, 0, self.L/2)
                self.mapdl.k(103, 0, self.bw, self.L/2)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(122, 0, 0, self.L/2)

                self.mapdl.k(201, self.bf, 0, self.L)
                self.mapdl.k(202, 0, 0, self.L)
                self.mapdl.k(203, 0, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(222, 0, 0, self.L)

                self.mapdl.a(1, 2, 102, 101)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 3, 103, 122)
                else:
                    self.mapdl.a(2, 3, 103, 102)

                self.mapdl.a(101, 102, 202, 201)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 103, 203, 222)
                else:
                    self.mapdl.a(102, 103, 203, 202)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, self.bf, 0, 0)
                self.mapdl.k(2, 0, 0, 0)
                self.mapdl.k(3, 0, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(22, 0, 0, 0)

                self.mapdl.k(101, self.bf, 0, self.Lshear)
                self.mapdl.k(102, 0, 0, self.Lshear)
                self.mapdl.k(103, 0, self.bw, self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(122, 0, 0, self.Lshear)

                self.mapdl.k(201, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(202, 0, 0, self.L - self.Lshear)
                self.mapdl.k(203, 0, self.bw, self.L - self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(222, 0, 0, self.L - self.Lshear)

                self.mapdl.k(301, self.bf, 0, self.L)
                self.mapdl.k(302, 0, 0, self.L)
                self.mapdl.k(303, 0, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(322, 0, 0, self.L)

                self.mapdl.a(1, 2, 102, 101)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 3, 103, 122)
                else:
                    self.mapdl.a(2, 3, 103, 102)

                self.mapdl.a(101, 102, 202, 201)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 103, 203, 222)
                else:
                    self.mapdl.a(102, 103, 203, 202)

                self.mapdl.a(201, 202, 302, 301)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(222, 203, 303, 322)
                else:
                    self.mapdl.a(202, 203, 303, 302)

        else:
            self.mapdl.k(1, self.bf, 0, 0)
            self.mapdl.k(2, 0, 0, 0)
            self.mapdl.k(3, 0, self.bw, 0)
            if self.connectionsIsNotRigid:
                self.mapdl.k(22, 0, 0, 0)

            self.mapdl.k(101, self.bf, 0, self.L)
            self.mapdl.k(102, 0, 0, self.L)
            self.mapdl.k(103, 0, self.bw, self.L)
            if self.connectionsIsNotRigid:
                self.mapdl.k(122, 0, 0, self.L)

            self.mapdl.a(1, 2, 102, 101)
            if self.connectionsIsNotRigid:
                self.mapdl.a(22, 3, 103, 122)
            else:
                self.mapdl.a(2, 3, 103, 102)

    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "X", 0)
        self.mapdl.aatt(self.materialAssignment[1], 1, 1, 0, 1)

        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", 0)
        self.mapdl.aatt(self.materialAssignment[0], 2, 1, 0, 2)   

    def setBoundaryConditions(self, boundaryConditions):
        if boundaryConditions['personalized']:
            for item in boundaryConditions["data"]:
                bc2 = item['2']
                self.mapdl.nsel("S", "LOC", "Y", 0)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc2:
                    if bc2[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)

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
    
    def setConnectionsIfAreNotRigid(self, elementSize):
        if self.connectionsIsNotRigid:
            self.mapdl.prep7()

            self.mapdl.allsel("ALL")
            cont = 1
            for i in range(int(self.L/elementSize + 1)):
                self.mapdl.nsel('S', 'LOC', 'Y', 0)
                self.mapdl.nsel('R', 'LOC', 'X', 0)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont},UX,arg_min{i},arg_max{i}')
                self.mapdl.run(f'CP,{cont + 1},UY,arg_min{i},arg_max{i}')
                self.mapdl.run(f'CP,{cont + 2},UZ,arg_min{i},arg_max{i}')
                self.mapdl.run(f'CP,{cont + 3},ROTX,arg_min{i},arg_max{i}')
                self.mapdl.run(f'CP,{cont + 4},ROTY,arg_min{i},arg_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg_min{i},arg_max{i}')
            
                cont += 5
        
            self.mapdl.run("/SOLU")

    def setBendingLoad(self, bendingLoadProperties):
        if 'points' in bendingLoadProperties:
            if bendingLoadProperties["points"] == 4:
                self.mapdl.fk(103, "FY", -1)
                self.mapdl.fk(203, "FY", -1)

            elif bendingLoadProperties["points"] == 3:
                self.mapdl.fk(103, "FY", -1)
        else:
            direction = 'M' + bendingLoadProperties["direction"]
            self.mapdl.run("/PREP7")
            self.mapdl.k(4, self.xcg, self.ycg, 0)
            self.mapdl.k(104, self.xcg, self.ycg, self.L)

            self.mapdl.k(5, self.bf, self.bw, 0)
            self.mapdl.k(105, self.bf, self.bw, self.L)

            self.mapdl.a(104,105,101,102)
            self.mapdl.a(104,102,103,105)

            self.mapdl.a(4,5,1,2)
            self.mapdl.a(4,2,3,5)

            self.mapdl.asel("ALL")
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.aatt(100, 3, 1, 0, 3)

            self.mapdl.mshkey(0)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.05)
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")

            self.mapdl.run("/SOLU")

            self.mapdl.fk(104, direction, 1)
            self.mapdl.fk(4, direction, - 1)
    
    def setNormalLoad(self, normalLoadProperties):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/(self.bf + self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", 1/(self.bf + self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.k(4, self.xcg, self.ycg, 0)
            self.mapdl.k(104, self.xcg, self.ycg, self.L)

            self.mapdl.k(5, self.bf, self.bw, 0)
            self.mapdl.k(105, self.bf, self.bw, self.L)

            self.mapdl.a(104,105,101,102)
            self.mapdl.a(104,102,103,105)

            self.mapdl.a(4,5,1,2)
            self.mapdl.a(4,2,3,5)

            self.mapdl.mshkey(0)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.05)
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")
            self.mapdl.aatt(100, 3, 1, 0, 3)

            self.mapdl.run("/SOLU")

            self.mapdl.fk(104, "FZ", -1)
            self.mapdl.fk(104, "MX", ey)
            self.mapdl.fk(104, "MY", ex)
            self.mapdl.fk(4, "FZ", 1)
            self.mapdl.fk(4, "MX", - ey)
            self.mapdl.fk(4, "MY", - ex)

    def setNewBendingLoad(self, bendingLoadProperties, newLoad):
        if 'points' in bendingLoadProperties:
            if bendingLoadProperties["points"] == 4:
                self.mapdl.fk(103, "FY", -newLoad)
                self.mapdl.fk(203, "FY", -newLoad)

            elif bendingLoadProperties["points"] == 3:
                self.mapdl.fk(103, "FY", -newLoad)
        else:
            direction = 'M' + bendingLoadProperties["direction"]
            self.mapdl.fk(104, direction, newLoad)
            self.mapdl.fk(4, direction, -newLoad)

    def setNewNormalLoad(self, normalLoadProperties, newLoad):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", newLoad /(self.bf + self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", newLoad /(self.bf + self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.fk(104, "FZ", -newLoad)
            self.mapdl.fk(104, "MX", ey * newLoad)
            self.mapdl.fk(104, "MY", ex * newLoad)
            self.mapdl.fk(4, "FZ", newLoad)
            self.mapdl.fk(4, "MX", - ey * newLoad)
            self.mapdl.fk(4, "MY", - ex * newLoad)