class TubularProfile:
    def __init__(self, mapdl, sectionProps, settings):
        self.mapdl = mapdl
        self.settings = settings
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
        self.connectionsIsNotRigid = not self.settings["general"]["connections"]["rigid"]
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, self.bf, self.bw, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(11, 0, 0, 0)
                    self.mapdl.k(22, self.bf, 0, 0)
                    self.mapdl.k(33, self.bf, self.bw, 0)
                    self.mapdl.k(44, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.L/2)
                self.mapdl.k(102, self.bf, 0, self.L/2)
                self.mapdl.k(103, self.bf, self.bw, self.L/2)
                self.mapdl.k(104, 0, self.bw, self.L/2)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(111, 0, 0, 0)
                    self.mapdl.k(122, self.bf, 0, 0)
                    self.mapdl.k(133, self.bf, self.bw, 0)
                    self.mapdl.k(144, 0, self.bw, 0)

                self.mapdl.k(201, 0, 0, self.L)
                self.mapdl.k(202, self.bf, self.bw, self.L)
                self.mapdl.k(203, self.bf, 0, self.L)
                self.mapdl.k(204, 0, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(211, 0, 0, 0)
                    self.mapdl.k(222, self.bf, 0, 0)
                    self.mapdl.k(233, self.bf, self.bw, 0)
                    self.mapdl.k(244, 0, self.bw, 0)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(3, 4, 104, 103)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 33, 133, 122)
                    self.mapdl.a(44, 11, 111, 144)
                else:
                    self.mapdl.a(2, 3, 103, 102)
                    self.mapdl.a(4, 1, 101, 104)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(103, 104, 204, 203)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 133, 233, 222)
                    self.mapdl.a(144, 111, 211, 244)
                else:
                    self.mapdl.a(102, 103, 203, 202)
                    self.mapdl.a(104, 101, 201, 204)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bf, 0, 0)
                self.mapdl.k(3, self.bf, self.bw, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(11, 0, 0, 0)
                    self.mapdl.k(22, self.bf, 0, 0)
                    self.mapdl.k(33, self.bf, self.bw, 0)
                    self.mapdl.k(44, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.Lshear)
                self.mapdl.k(102, self.bf, 0, self.Lshear)
                self.mapdl.k(103, self.bf, self.bw, self.Lshear)
                self.mapdl.k(104, 0, self.bw, self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(111, 0, 0, self.Lshear)
                    self.mapdl.k(122, self.bf, 0, self.Lshear)
                    self.mapdl.k(133, self.bf, self.bw, self.Lshear)
                    self.mapdl.k(144, 0, self.bw, self.Lshear)

                self.mapdl.k(201, 0, 0, self.L - self.Lshear)
                self.mapdl.k(202, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(203, self.bf, self.bw, self.L - self.Lshear)
                self.mapdl.k(204, 0, self.bw, self.L - self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(211, 0, 0, self.L - self.Lshear)
                    self.mapdl.k(222, self.bf, 0, self.L - self.Lshear)
                    self.mapdl.k(233, self.bf, self.bw, self.L - self.Lshear)
                    self.mapdl.k(244, 0, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, 0, 0, self.L)
                self.mapdl.k(302, self.bf, 0, self.L)
                self.mapdl.k(303, self.bf, self.bw, self.L)
                self.mapdl.k(304, 0, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(311, 0, 0, self.L)
                    self.mapdl.k(322, self.bf, 0, self.L)
                    self.mapdl.k(333, self.bf, self.bw, self.L)
                    self.mapdl.k(344, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(3, 4, 104, 103)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 33, 133, 122)
                    self.mapdl.a(44, 11, 111, 144)
                else:
                    self.mapdl.a(2, 3, 103, 102)
                    self.mapdl.a(4, 1, 101, 104)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(103, 104, 204, 203)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 133, 233, 222)
                    self.mapdl.a(144, 111, 211, 244)
                else:
                    self.mapdl.a(102, 103, 203, 202)
                    self.mapdl.a(104, 101, 201, 204)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(203, 204, 304, 303)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(222, 233, 333, 322)
                    self.mapdl.a(244, 211, 311, 344)
                else:
                    self.mapdl.a(202, 203, 303, 302)
                    self.mapdl.a(204, 201, 301, 304)
        else:
            self.mapdl.k(1, 0, 0, 0)
            self.mapdl.k(2, self.bf, 0, 0)
            self.mapdl.k(3, self.bf, self.bw, 0)
            self.mapdl.k(4, 0, self.bw, 0)
            if self.connectionsIsNotRigid:
                    self.mapdl.k(11, 0, 0, 0)
                    self.mapdl.k(22, self.bf, 0, 0)
                    self.mapdl.k(33, self.bf, self.bw, 0)
                    self.mapdl.k(44, 0, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, self.bf, 0, self.L)
            self.mapdl.k(103, self.bf, self.bw, self.L)
            self.mapdl.k(104, 0, self.bw, self.L)
            if self.connectionsIsNotRigid:
                    self.mapdl.k(111, 0, 0, self.L)
                    self.mapdl.k(122, self.bf, 0, self.L)
                    self.mapdl.k(133, self.bf, self.bw, self.L)
                    self.mapdl.k(144, 0, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(3, 4, 104, 103)
            if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 33, 133, 122)
                    self.mapdl.a(44, 11, 111, 144)
            else:
                    self.mapdl.a(2, 3, 103, 102)
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
            for item in boundaryConditions["data"]:
                bc2 = item['2']
                self.mapdl.nsel("S", "LOC", "X", 0)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc2:
                    if bc2[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)
                
                self.mapdl.nsel("S", "LOC", "X", self.bf)
                self.mapdl.nsel("R", "LOC", "Z", item["z"])
                for key in bc2:
                    if bc2[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)

                bc1 = item['1']
                self.mapdl.nsel("S", "LOC", "Z", item["z"])
                self.mapdl.nsel("R", "LOC", "Y", 0)
                for key in bc1:
                    if bc1[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)
                
                self.mapdl.nsel("S", "LOC", "Z", item["z"])
                self.mapdl.nsel("R", "LOC", "Y", self.bw)
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


                self.mapdl.nsel('S', 'LOC', 'Y', 0)
                self.mapdl.nsel('R', 'LOC', 'X', self.bf)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg2_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg2_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont + 5},UX,arg2_min{i},arg2_max{i}')
                self.mapdl.run(f'CP,{cont + 6},UY,arg2_min{i},arg2_max{i}')
                self.mapdl.run(f'CP,{cont + 7},UZ,arg2_min{i},arg2_max{i}')
                self.mapdl.run(f'CP,{cont + 8},ROTX,arg2_min{i},arg2_max{i}')
                self.mapdl.run(f'CP,{cont + 9},ROTY,arg2_min{i},arg2_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg2_min{i},arg2_max{i}')


                self.mapdl.nsel('S', 'LOC', 'Y', self.bw)
                self.mapdl.nsel('R', 'LOC', 'X', self.bf)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg3_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg3_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont + 10},UX,arg3_min{i},arg3_max{i}')
                self.mapdl.run(f'CP,{cont + 11},UY,arg3_min{i},arg3_max{i}')
                self.mapdl.run(f'CP,{cont + 12},UZ,arg3_min{i},arg3_max{i}')
                self.mapdl.run(f'CP,{cont + 13},ROTX,arg3_min{i},arg3_max{i}')
                self.mapdl.run(f'CP,{cont + 14},ROTY,arg3_min{i},arg3_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg3_min{i},arg3_max{i}')


                self.mapdl.nsel('S', 'LOC', 'Y', self.bw)
                self.mapdl.nsel('R', 'LOC', 'X', 0)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg4_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg4_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont + 15},UX,arg4_min{i},arg4_max{i}')
                self.mapdl.run(f'CP,{cont + 16},UY,arg4_min{i},arg4_max{i}')
                self.mapdl.run(f'CP,{cont + 17},UZ,arg4_min{i},arg4_max{i}')
                self.mapdl.run(f'CP,{cont + 18},ROTX,arg4_min{i},arg4_max{i}')
                self.mapdl.run(f'CP,{cont + 19},ROTY,arg4_min{i},arg4_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg4_min{i},arg4_max{i}')
            
                cont += 20
        
            self.mapdl.run("/SOLU")
    
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
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/(2 * self.bf + 2 * self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", 1/(2 * self.bf + 2 * self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.k(5, self.bf / 2, self.bw / 2, 0)
            self.mapdl.k(105, self.bf / 2, self.bw / 2, self.L)
            self.mapdl.a(105,101,102,103)
            self.mapdl.a(105,103,104,101)

            self.mapdl.a(5,1,2,3)
            self.mapdl.a(5,3,4,1)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(0)
            self.mapdl.aesize("ALL", 0.05)
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")

            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.run("/SOLU")

            self.mapdl.fk(105, "FZ", -1)
            self.mapdl.fk(105, "MX", ex)
            self.mapdl.fk(105, "MY", ey)
            self.mapdl.fk(5, "FZ", 1)
            self.mapdl.fk(5, "MX", - ex)
            self.mapdl.fk(5, "MY", - ey)