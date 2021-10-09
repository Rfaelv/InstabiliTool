class RackProfile:
    def __init__(self, mapdl, sectionProps, settings):
        self.mapdl = mapdl
        self.settings = settings
        self.d = sectionProps['d']
        self.b = sectionProps['b']
        self.t = sectionProps['t']
        self.z = sectionProps['z']
        self.y = sectionProps['y']
        self.L = sectionProps['L']
        self.bw = self.d - self.t
        self.bf = self.b - self.t
        self.zf = self.z - self.t
        self.yf = self.y - self.t / 2

        self.materialAssignment = sectionProps["materialAssignment"]

        self.xcg = (2 * (self.bf * self.t * self.bf / 2 + self.zf * self.t * (self.b - self.t) + self.y * self.t * (self.b + self.y / 2 - 3 * self.t / 2))) / (((self.bw - self.t) + 2 * (self.bf + self.zf + self.y)) * self.t)
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

        self.mapdl.sectype(4, "SHELL", "", "plateLoad")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(0.1, 100)

    def createProfile(self, loadType, loadProps):
        self.connectionsIsNotRigid = not self.settings["general"]["connections"]["rigid"]
        if loadType['bending'] and 'points' in loadProps:
            if loadProps['points'] == 3:
                self.mapdl.k(1, self.bf + self.yf, self.zf, 0)
                self.mapdl.k(2, self.bf, self.zf, 0)
                self.mapdl.k(3, self.bf, 0, 0)
                self.mapdl.k(4, 0, 0, 0)
                self.mapdl.k(5, 0, self.bw, 0)
                self.mapdl.k(6, self.bf, self.bw, 0)
                self.mapdl.k(7, self.bf, self.bw - self.zf, 0)
                self.mapdl.k(8, self.bf + self.yf, self.bw - self.zf, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(22, self.bf, self.zf, 0)
                    self.mapdl.k(33, self.bf, 0, 0)
                    self.mapdl.k(44, 0, 0, 0)
                    self.mapdl.k(55, 0, self.bw, 0)
                    self.mapdl.k(66, self.bf, self.bw, 0)
                    self.mapdl.k(77, self.bf, self.bw - self.zf, 0)

                self.mapdl.k(101, self.bf + self.yf, self.zf, self.L/2)
                self.mapdl.k(102, self.bf, self.zf, self.L/2)
                self.mapdl.k(103, self.bf, 0, self.L/2)
                self.mapdl.k(104, 0, 0, self.L/2)
                self.mapdl.k(105, 0, self.bw, self.L/2)
                self.mapdl.k(106, self.bf, self.bw, self.L/2)
                self.mapdl.k(107, self.bf, self.bw - self.zf, self.L/2)
                self.mapdl.k(108, self.bf + self.yf, self.bw - self.zf, self.L/2)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(122, self.bf, self.zf, self.L/2)
                    self.mapdl.k(133, self.bf, 0, self.L/2)
                    self.mapdl.k(144, 0, 0, self.L/2)
                    self.mapdl.k(155, 0, self.bw, self.L/2)
                    self.mapdl.k(166, self.bf, self.bw, self.L/2)
                    self.mapdl.k(177, self.bf, self.bw - self.zf, self.L/2)

                self.mapdl.k(201, self.bf + self.yf, self.zf, self.L)
                self.mapdl.k(202, self.bf, self.zf, self.L)
                self.mapdl.k(203, self.bf, 0, self.L)
                self.mapdl.k(204, 0, 0, self.L)
                self.mapdl.k(205, 0, self.bw, self.L)
                self.mapdl.k(206, self.bf, self.bw, self.L)
                self.mapdl.k(207, self.bf, self.bw - self.zf, self.L)
                self.mapdl.k(208, self.bf + self.yf, self.bw - self.zf, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(222, self.bf, self.zf, self.L)
                    self.mapdl.k(233, self.bf, 0, self.L)
                    self.mapdl.k(244, 0, 0, self.L)
                    self.mapdl.k(255, 0, self.bw, self.L)
                    self.mapdl.k(266, self.bf, self.bw, self.L)
                    self.mapdl.k(277, self.bf, self.bw - self.zf, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(5, 6, 106, 105)
                self.mapdl.a(7, 8, 108, 107)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 33, 133, 122)
                    self.mapdl.a(44, 55, 155, 144)
                    self.mapdl.a(66, 77, 177, 166)
                else:
                    self.mapdl.a(2, 3, 103, 102)
                    self.mapdl.a(4, 5, 105, 104)
                    self.mapdl.a(6, 7, 107, 106)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(105, 106, 206, 205)
                self.mapdl.a(107, 108, 208, 207)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 133, 233, 222)
                    self.mapdl.a(144, 155, 255, 244)
                    self.mapdl.a(166, 177, 277, 266)
                else:
                    self.mapdl.a(102, 103, 203, 202)
                    self.mapdl.a(104, 105, 205, 204)
                    self.mapdl.a(106, 107, 207, 206)

            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, self.bf + self.yf, self.zf, 0)
                self.mapdl.k(2, self.bf, self.zf, 0)
                self.mapdl.k(3, self.bf, 0, 0)
                self.mapdl.k(4, 0, 0, 0)
                self.mapdl.k(5, 0, self.bw, 0)
                self.mapdl.k(6, self.bf, self.bw, 0)
                self.mapdl.k(7, self.bf, self.bw - self.zf, 0)
                self.mapdl.k(8, self.bf + self.yf, self.bw - self.zf, 0)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(22, self.bf, self.zf, 0)
                    self.mapdl.k(33, self.bf, 0, 0)
                    self.mapdl.k(44, 0, 0, 0)
                    self.mapdl.k(55, 0, self.bw, 0)
                    self.mapdl.k(66, self.bf, self.bw, 0)
                    self.mapdl.k(77, self.bf, self.bw - self.zf, 0)

                self.mapdl.k(101, self.bf + self.yf, self.zf, self.Lshear)
                self.mapdl.k(102, self.bf, self.zf, self.Lshear)
                self.mapdl.k(103, self.bf, 0, self.Lshear)
                self.mapdl.k(104, 0, 0, self.Lshear)
                self.mapdl.k(105, 0, self.bw, self.Lshear)
                self.mapdl.k(106, self.bf, self.bw, self.Lshear)
                self.mapdl.k(107, self.bf, self.bw - self.zf, self.Lshear)
                self.mapdl.k(108, self.bf + self.yf, self.bw - self.zf, self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(122, self.bf, self.zf, self.Lshear)
                    self.mapdl.k(133, self.bf, 0, self.Lshear)
                    self.mapdl.k(144, 0, 0, self.Lshear)
                    self.mapdl.k(155, 0, self.bw, self.Lshear)
                    self.mapdl.k(166, self.bf, self.bw, self.Lshear)
                    self.mapdl.k(177, self.bf, self.bw - self.zf, self.Lshear)

                self.mapdl.k(201, self.bf + self.yf, self.zf, self.L - self.Lshear)
                self.mapdl.k(202, self.bf, self.zf, self.L - self.Lshear)
                self.mapdl.k(203, self.bf, 0, self.L - self.Lshear)
                self.mapdl.k(204, 0, 0, self.L - self.Lshear)
                self.mapdl.k(205, 0, self.bw, self.L - self.Lshear)
                self.mapdl.k(206, self.bf, self.bw, self.L - self.Lshear)
                self.mapdl.k(207, self.bf, self.bw - self.zf, self.L - self.Lshear)
                self.mapdl.k(208, self.bf + self.yf, self.bw - self.zf, self.L - self.Lshear)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(222, self.bf, self.zf, self.L - self.Lshear)
                    self.mapdl.k(233, self.bf, 0, self.L - self.Lshear)
                    self.mapdl.k(244, 0, 0, self.L - self.Lshear)
                    self.mapdl.k(255, 0, self.bw, self.L - self.Lshear)
                    self.mapdl.k(266, self.bf, self.bw, self.L - self.Lshear)
                    self.mapdl.k(277, self.bf, self.bw - self.zf, self.L - self.Lshear)

                self.mapdl.k(301, self.bf + self.yf, self.zf, self.L)
                self.mapdl.k(302, self.bf, self.zf, self.L)
                self.mapdl.k(303, self.bf, 0, self.L)
                self.mapdl.k(304, 0, 0, self.L)
                self.mapdl.k(305, 0, self.bw, self.L)
                self.mapdl.k(306, self.bf, self.bw, self.L)
                self.mapdl.k(307, self.bf, self.bw - self.zf, self.L)
                self.mapdl.k(308, self.bf + self.yf, self.bw - self.zf, self.L)
                if self.connectionsIsNotRigid:
                    self.mapdl.k(322, self.bf, self.zf, self.L)
                    self.mapdl.k(333, self.bf, 0, self.L)
                    self.mapdl.k(344, 0, 0, self.L)
                    self.mapdl.k(355, 0, self.bw, self.L)
                    self.mapdl.k(366, self.bf, self.bw, self.L)
                    self.mapdl.k(377, self.bf, self.bw - self.zf, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(3, 4, 104, 103)
                self.mapdl.a(5, 6, 106, 105)
                self.mapdl.a(7, 8, 108, 107)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(22, 33, 133, 122)
                    self.mapdl.a(44, 55, 155, 144)
                    self.mapdl.a(66, 77, 177, 166)
                else:
                    self.mapdl.a(2, 3, 103, 102)
                    self.mapdl.a(4, 5, 105, 104)
                    self.mapdl.a(6, 7, 107, 106)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(103, 104, 204, 203)
                self.mapdl.a(105, 106, 206, 205)
                self.mapdl.a(107, 108, 208, 207)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(122, 133, 233, 222)
                    self.mapdl.a(144, 155, 255, 244)
                    self.mapdl.a(166, 177, 277, 266)
                else:
                    self.mapdl.a(102, 103, 203, 202)
                    self.mapdl.a(104, 105, 205, 204)
                    self.mapdl.a(106, 107, 207, 206)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(203, 204, 304, 303)
                self.mapdl.a(205, 206, 306, 305)
                self.mapdl.a(207, 208, 308, 307)
                if self.connectionsIsNotRigid:
                    self.mapdl.a(222, 233, 333, 322)
                    self.mapdl.a(244, 255, 355, 344)
                    self.mapdl.a(266, 277, 377, 366)
                else:
                    self.mapdl.a(202, 203, 303, 302)
                    self.mapdl.a(204, 205, 305, 304)
                    self.mapdl.a(206, 207, 307, 306)

        else:
            self.mapdl.k(1, self.bf + self.yf, self.zf, 0)
            self.mapdl.k(2, self.bf, self.zf, 0)
            self.mapdl.k(3, self.bf, 0, 0)
            self.mapdl.k(4, 0, 0, 0)
            self.mapdl.k(5, 0, self.bw, 0)
            self.mapdl.k(6, self.bf, self.bw, 0)
            self.mapdl.k(7, self.bf, self.bw - self.zf, 0)
            self.mapdl.k(8, self.bf + self.yf, self.bw - self.zf, 0)
            if self.connectionsIsNotRigid:
                self.mapdl.k(22, self.bf, self.zf, 0)
                self.mapdl.k(33, self.bf, 0, 0)
                self.mapdl.k(44, 0, 0, 0)
                self.mapdl.k(55, 0, self.bw, 0)
                self.mapdl.k(66, self.bf, self.bw, 0)
                self.mapdl.k(77, self.bf, self.bw - self.zf, 0)

            self.mapdl.k(101, self.bf + self.yf, self.zf, self.L)
            self.mapdl.k(102, self.bf, self.zf, self.L)
            self.mapdl.k(103, self.bf, 0, self.L)
            self.mapdl.k(104, 0, 0, self.L)
            self.mapdl.k(105, 0, self.bw, self.L)
            self.mapdl.k(106, self.bf, self.bw, self.L)
            self.mapdl.k(107, self.bf, self.bw - self.zf, self.L)
            self.mapdl.k(108, self.bf + self.yf, self.bw - self.zf, self.L)
            if self.connectionsIsNotRigid:
                self.mapdl.k(122, self.bf, self.zf, self.L)
                self.mapdl.k(133, self.bf, 0, self.L)
                self.mapdl.k(144, 0, 0, self.L)
                self.mapdl.k(155, 0, self.bw, self.L)
                self.mapdl.k(166, self.bf, self.bw, self.L)
                self.mapdl.k(177, self.bf, self.bw - self.zf, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(3, 4, 104, 103)
            self.mapdl.a(5, 6, 106, 105)
            self.mapdl.a(7, 8, 108, 107)
            if self.connectionsIsNotRigid:
                self.mapdl.a(22, 33, 133, 122)
                self.mapdl.a(44, 55, 155, 144)
                self.mapdl.a(66, 77, 177, 166)
            else:
                self.mapdl.a(2, 3, 103, 102)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(6, 7, 107, 106)

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
    
    def setConnectionsIfAreNotRigid(self, elementSize):
        if self.connectionsIsNotRigid:
            self.mapdl.prep7()

            self.mapdl.allsel("ALL")
            cont = 1
            for i in range(int(self.L/elementSize + 1)):
                self.mapdl.nsel('S', 'LOC', 'Y', self.zf)
                self.mapdl.nsel('R', 'LOC', 'X', self.bf)
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


                self.mapdl.nsel('S', 'LOC', 'Y', 0)
                self.mapdl.nsel('R', 'LOC', 'X', 0)
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


                self.mapdl.nsel('S', 'LOC', 'Y', self.bw)
                self.mapdl.nsel('R', 'LOC', 'X', self.bf)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg5_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg5_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont + 20},UX,arg5_min{i},arg5_max{i}')
                self.mapdl.run(f'CP,{cont + 21},UY,arg5_min{i},arg5_max{i}')
                self.mapdl.run(f'CP,{cont + 22},UZ,arg5_min{i},arg5_max{i}')
                self.mapdl.run(f'CP,{cont + 23},ROTX,arg5_min{i},arg5_max{i}')
                self.mapdl.run(f'CP,{cont + 24},ROTY,arg5_min{i},arg5_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg5_min{i},arg5_max{i}')


                self.mapdl.nsel('S', 'LOC', 'Y', self.bw - self.zf)
                self.mapdl.nsel('R', 'LOC', 'X', self.bf)
                self.mapdl.nsel('R', 'LOC', 'Z', i*elementSize)

                self.mapdl.run(f'*GET,arg6_max{i},NODE,0,NUM,MAX')
                self.mapdl.run(f'*GET,arg6_min{i},NODE,0,NUM,MIN')

                self.mapdl.run(f'CP,{cont + 25},UX,arg6_min{i},arg6_max{i}')
                self.mapdl.run(f'CP,{cont + 26},UY,arg6_min{i},arg6_max{i}')
                self.mapdl.run(f'CP,{cont + 27},UZ,arg6_min{i},arg6_max{i}')
                self.mapdl.run(f'CP,{cont + 28},ROTX,arg6_min{i},arg6_max{i}')
                self.mapdl.run(f'CP,{cont + 29},ROTY,arg6_min{i},arg6_max{i}')

                self.mapdl.type(2)
                self.mapdl.real(2)
                self.mapdl.run(f'E,arg6_min{i},arg6_max{i}')
            
                cont += 30
        
            self.mapdl.run("/SOLU")
    
    def setBendingLoad(self, bendingLoadProperties):
        if 'points' in bendingLoadProperties:
            if bendingLoadProperties["points"] == 4:
                self.mapdl.fk(105, "FY", -1)
                self.mapdl.fk(205, "FY", -1)

            elif bendingLoadProperties["points"] == 3:
                self.mapdl.fk(105, "FY", -1)
        else:
            direction = 'M' + bendingLoadProperties["direction"]
            self.mapdl.run("/PREP7")
            self.mapdl.k(9, self.xcg, self.ycg, 0)
            self.mapdl.k(109, self.xcg, self.ycg, self.L)

            self.mapdl.a(109,102,103,104,105,106,107)
            self.mapdl.a(109,102,101,108,107)

            self.mapdl.a(9,2,3,4,5,6,7)
            self.mapdl.a(9,2,1,8,7)

            self.mapdl.asel("ALL")
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.05)
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")

            self.mapdl.run("/SOLU")

            self.mapdl.fk(109, direction, 1)
            self.mapdl.fk(9, direction, - 1)
    
    def setNormalLoad(self, normalLoadProperties):
        if normalLoadProperties["type"] == "distributed":
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.sf("ALL", "PRES", 1/(2 * (self.bf + self.zf + self.yf) + self.bw))

            self.mapdl.nsel("S", "LOC", "Z", self.L)
            self.mapdl.sf("ALL", "PRES", 1/(2 * (self.bf + self.zf + self.yf) + self.bw))

        elif normalLoadProperties["type"] == "point":
            ex = normalLoadProperties["x"]
            ey = normalLoadProperties["y"]

            self.mapdl.run("/PREP7")
            self.mapdl.k(9, self.xcg, self.ycg, 0)
            self.mapdl.k(109, self.xcg, self.ycg, self.L)

            self.mapdl.a(109,102,103,104,105,106,107)
            self.mapdl.a(109,102,101,108,107)

            self.mapdl.a(9,2,3,4,5,6,7)
            self.mapdl.a(9,2,1,8,7)

            self.mapdl.asel("ALL")
            self.mapdl.asel("S", "LOC", "Z", 0)
            self.mapdl.asel("A", "LOC", "Z", self.L)
            self.mapdl.aatt(100, 4, 1, 0, 4)

            self.mapdl.mshkey(2)
            self.mapdl.mshape(1)
            self.mapdl.aesize("ALL", 0.01)
            self.mapdl.nsel("S", "LOC", "Z", 0)
            self.mapdl.nsel("A", "LOC", "Z", self.L)
            self.mapdl.amesh("ALL")

            self.mapdl.run("/SOLU")

            self.mapdl.fk(109, "FZ", -1)
            self.mapdl.fk(109, "MX", ey)
            self.mapdl.fk(109, "MY", ex)
            self.mapdl.fk(9, "FZ", 1)
            self.mapdl.fk(9, "MX", - ey)
            self.mapdl.fk(9, "MY", - ex)