class IProfile:
    def __init__(self, mapdl, sectionProps, settings):
        self.mapdl = mapdl
        self.settings = settings
        self.d = sectionProps['d']
        self.bfs = sectionProps['bfs']
        self.bfi = sectionProps['bfi']
        self.tw = sectionProps['tw']
        self.tfs = sectionProps['tfs']
        self.tfi = sectionProps['tfi']
        self.L = sectionProps['L']
        self.bw = self.d - self.tfi/2 - self.tfs/2

        self.materialAssignment = sectionProps["materialAssignment"]

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "flangeS")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tfs, self.materialAssignment[0])
        self.mapdl.sectype(2, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tw, self.materialAssignment[1])
        self.mapdl.sectype(3, "SHELL", "", "flangeI")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tfi, self.materialAssignment[2])

        self.mapdl.sectype(4, "SHELL", "", "plateLoad")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(0.1, 100)

    def createProfile(self, loadType, loadProps):
        self.connectionsIsNotRigid = not self.settings["general"]["connections"]["rigid"]
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bfi/2, 0, 0)
                self.mapdl.k(3, - self.bfi/2, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bfs/2, self.bw, 0)
                self.mapdl.k(6, - self.bfs/2, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(11, 0, 0, 0)
                    self.mapdl.k(44, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.L/2)
                self.mapdl.k(102, self.bfi/2, 0, self.L/2)
                self.mapdl.k(103, - self.bfi/2, 0, self.L/2)
                self.mapdl.k(104, 0, self.bw, self.L/2)
                self.mapdl.k(105, self.bfs/2, self.bw, self.L/2)
                self.mapdl.k(106, - self.bfs/2, self.bw, self.L/2)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(111, 0, 0, self.L/2)
                    self.mapdl.k(144, 0, self.bw, self.L/2)

                self.mapdl.k(201, 0, 0, self.L)
                self.mapdl.k(202, self.bfi/2, 0, self.L)
                self.mapdl.k(203, - self.bfi/2, 0, self.L)
                self.mapdl.k(204, 0, self.bw, self.L)
                self.mapdl.k(205, self.bfs/2, self.bw, self.L)
                self.mapdl.k(206, - self.bfs/2, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(211, 0, 0, self.L)
                    self.mapdl.k(244, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(1, 3, 103, 101)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(4, 6, 106, 104)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(11, 44, 144, 111)
                else:
                    self.mapdl.a(1, 4, 104, 101)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(101, 103, 203, 201)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(104, 106, 206, 204)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(111, 144, 244, 211)
                else:
                    self.mapdl.a(101, 104, 204, 201)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bfi/2, 0, 0)
                self.mapdl.k(3, - self.bfi/2, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bfs/2, self.bw, 0)
                self.mapdl.k(6, - self.bfs/2, self.bw, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(11, 0, 0, 0)
                    self.mapdl.k(44, 0, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.Lshear)
                self.mapdl.k(102, self.bfi/2, 0, self.Lshear)
                self.mapdl.k(103, - self.bfi/2, 0, self.Lshear)
                self.mapdl.k(104, 0, self.bw, self.Lshear)
                self.mapdl.k(105, self.bfs/2, self.bw, self.Lshear)
                self.mapdl.k(106, - self.bfs/2, self.bw, self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(111, 0, 0, self.Lshear)
                    self.mapdl.k(144, 0, self.bw, self.Lshear)

                self.mapdl.k(201, 0, 0, self.L - self.Lshear)
                self.mapdl.k(202, self.bfi/2, 0, self.L - self.Lshear)
                self.mapdl.k(203, - self.bfi/2, 0, self.L - self.Lshear)
                self.mapdl.k(204, 0, self.bw, self.L - self.Lshear)
                self.mapdl.k(205, self.bfs/2, self.bw, self.L - self.Lshear)
                self.mapdl.k(206, - self.bfs/2, self.bw, self.L - self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(211, 0, 0, self.L - self.Lshear)
                    self.mapdl.k(244, 0, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, 0, 0, self.L)
                self.mapdl.k(302, self.bfi/2, 0, self.L)
                self.mapdl.k(303, - self.bfi/2, 0, self.L)
                self.mapdl.k(304, 0, self.bw, self.L)
                self.mapdl.k(305, self.bfs/2, self.bw, self.L)
                self.mapdl.k(306, - self.bfs/2, self.bw, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(311, 0, 0, self.L)
                    self.mapdl.k(344, 0, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(1, 3, 103, 101)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(4, 6, 106, 104)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(11, 44, 144, 111)
                else:
                    self.mapdl.a(1, 4, 104, 101)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(101, 103, 203, 201)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(104, 106, 206, 204)
                # self.mapdl.a(101, 104, 204, 201)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(111, 144, 244, 211)
                else:
                    self.mapdl.a(101, 104, 204, 201)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(201, 203, 303, 301)
                self.mapdl.a(204, 205, 305, 304)
                self.mapdl.a(204, 206, 306, 304)
                # self.mapdl.a(201, 204, 304, 301)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(211, 244, 344, 311)
                else:
                    self.mapdl.a(201, 204, 304, 301)
        else:
            self.mapdl.k(1, 0, 0, 0)
            self.mapdl.k(2, self.bfi/2, 0, 0)
            self.mapdl.k(3, - self.bfi/2, 0, 0)
            self.mapdl.k(4, 0, self.bw/2, 0)
            self.mapdl.k(5, 0, self.bw, 0)
            self.mapdl.k(6, self.bfs/2, self.bw, 0)
            self.mapdl.k(7, - self.bfs/2, self.bw, 0)
            if self.connectionsIsNotRigid:
                self.mapdl.k(11, 0, 0, 0)
                self.mapdl.k(55, 0, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, self.bfi/2, 0, self.L)
            self.mapdl.k(103, - self.bfi/2, 0, self.L)
            self.mapdl.k(104, 0, self.bw/2, self.L)
            self.mapdl.k(105, 0, self.bw, self.L)
            self.mapdl.k(106, self.bfs/2, self.bw, self.L)
            self.mapdl.k(107, - self.bfs/2, self.bw, self.L)
            if self.connectionsIsNotRigid:
                self.mapdl.k(111, 0, 0, self.L)
                self.mapdl.k(155, 0, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(1, 3, 103, 101)
            self.mapdl.a(5, 6, 106, 105)
            self.mapdl.a(5, 7, 107, 105)
            if self.connectionsIsNotRigid:
                self.mapdl.a(111, 144, 244, 211)
                self.mapdl.a(144, 155, 255, 244)
            else:
                self.mapdl.a(1, 4, 104, 101)
                self.mapdl.a(4, 5, 105, 104)

            # self.mapdl.a(104,105,106,102,101,104)
            # self.mapdl.a(104,105,107,103,101,104)

            # self.mapdl.a(4,5,7,3,1,4)
            # self.mapdl.a(4,5,7,3,1,4)
   
    def setMaterial(self):
        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", self.bw)
        self.mapdl.aatt(self.materialAssignment[0], 1, 1, 0, 1)

        self.mapdl.asel("ALL")
        self.mapdl.asel("S", "LOC", "Y", 0)
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
                self.mapdl.nsel("S", "LOC", "Z", item["z"])
                self.mapdl.nsel("R", "LOC", "Y", self.bw)
                for key in bc1:
                    if bc1[key] and key != "all":
                        self.mapdl.d('ALL', key, 0)

                bc3 = item['3']
                self.mapdl.nsel("S", "LOC", "Z", item["z"])
                self.mapdl.nsel("R", "LOC", "Y", 0)
                for key in bc3:
                    if bc3[key] and key != 'all':
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
                self.mapdl.nsel('S', 'LOC', 'Y', self.bw)
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
                self.mapdl.nsel('R', 'LOC', 'X', 0)
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
            
                cont += 10
        
            self.mapdl.run("/SOLU")

    def setBendingLoad(self, bendingLoadProperties):
        if bendingLoadProperties["points"] == 4:
            self.mapdl.fk(104, "FY", -1)
            self.mapdl.fk(204, "FY", -1)

        elif bendingLoadProperties["points"] == 3:
            self.mapdl.fk(104, "FY", -1)
    
    def setNormalLoad(self, normalLoadProperties):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/(self.bfi + self.bfs + self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", 1/(self.bfi + self.bfs + self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.a(104,105,106,102,101,104)
            self.mapdl.a(104,105,107,103,101,104)

            self.mapdl.a(4,5,6,2,1,4)
            self.mapdl.a(4,5,7,3,1,4)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(0)
            self.mapdl.aesize("ALL", 0.05)
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")

            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.run("/SOLU")

            self.mapdl.fk(104, "FZ", -1)
            self.mapdl.fk(104, "MX", ex)
            self.mapdl.fk(104, "MY", ey)
            self.mapdl.fk(4, "FZ", 1)
            self.mapdl.fk(4, "MX", - ex)
            self.mapdl.fk(4, "MY", - ey)
        # self.mapdl.run("/PREP7")
        # self.mapdl.n(50000, 0, self.bw/2, self.L)
        # self.mapdl.run("/SOLU")

        # self.mapdl.nsel("S", "LOC", "Z", self.L)
        # self.mapdl.sf("ALL", "PRESS", 1/(self.bfi + self.bfs + self.bw)) # Funciona para o caso de carga centrada

        # self.mapdl.cp("UZ", "ALL")
        # self.mapdl.fk(104, "FZ", -1)
        # self.mapdl.fk(4, "FZ", 1)
        # self.mapdl.fk(102, "FZ", -1)
        # self.mapdl.fk(104, "MX", 0.145)
        # self.mapdl.fk(104, "MY", 0.145)
        # self.mapdl.open_gui()
