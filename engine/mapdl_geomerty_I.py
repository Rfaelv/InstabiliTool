class IProfile:
    def __init__(self, mapdl, sectionProps):
        self.mapdl = mapdl
        self.d = sectionProps['d']
        self.bfs = sectionProps['bfs']
        self.bfi = sectionProps['bfi']
        self.tw = sectionProps['tw']
        self.tfs = sectionProps['tfs']
        self.tfi = sectionProps['tfi']
        self.L = sectionProps['L']
        self.bw = self.d - self.tfi/2 - self.tfs/2

    def createSection(self):
        self.mapdl.sectype(1, "SHELL", "", "flangeS")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tfs, 1)
        self.mapdl.sectype(2, "SHELL", "", "web")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tw, 2)
        self.mapdl.sectype(3, "SHELL", "", "flangeI")
        self.mapdl.secoffset("MID")
        self.mapdl.secdata(self.tfi, 3)

    def createProfile(self, loadType, loadProps):
        if loadType['bending']:
            if loadProps['points'] == 3:
                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bfi/2, 0, 0)
                self.mapdl.k(3, - self.bfi/2, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bfs/2, self.bw, 0)
                self.mapdl.k(6, - self.bfs/2, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.L/2)
                self.mapdl.k(102, self.bfi/2, 0, self.L/2)
                self.mapdl.k(103, - self.bfi/2, 0, self.L/2)
                self.mapdl.k(104, 0, self.bw, self.L/2)
                self.mapdl.k(105, self.bfs/2, self.bw, self.L/2)
                self.mapdl.k(106, - self.bfs/2, self.bw, self.L/2)

                self.mapdl.k(201, 0, 0, self.L)
                self.mapdl.k(202, self.bfi/2, 0, self.L)
                self.mapdl.k(203, - self.bfi/2, 0, self.L)
                self.mapdl.k(204, 0, self.bw, self.L)
                self.mapdl.k(205, self.bfs/2, self.bw, self.L)
                self.mapdl.k(206, - self.bfs/2, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(1, 3, 103, 101)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(4, 6, 106, 104)
                self.mapdl.a(1, 4, 104, 101)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(101, 103, 203, 201)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(104, 106, 206, 204)
                self.mapdl.a(101, 104, 204, 201)
            else:
                self.Lshear = loadProps['Lshear']

                self.mapdl.k(1, 0, 0, 0)
                self.mapdl.k(2, self.bfi/2, 0, 0)
                self.mapdl.k(3, - self.bfi/2, 0, 0)
                self.mapdl.k(4, 0, self.bw, 0)
                self.mapdl.k(5, self.bfs/2, self.bw, 0)
                self.mapdl.k(6, - self.bfs/2, self.bw, 0)

                self.mapdl.k(101, 0, 0, self.Lshear)
                self.mapdl.k(102, self.bfi/2, 0, self.Lshear)
                self.mapdl.k(103, - self.bfi/2, 0, self.Lshear)
                self.mapdl.k(104, 0, self.bw, self.Lshear)
                self.mapdl.k(105, self.bfs/2, self.bw, self.Lshear)
                self.mapdl.k(106, - self.bfs/2, self.bw, self.Lshear)

                self.mapdl.k(201, 0, 0, self.L - self.Lshear)
                self.mapdl.k(202, self.bfi/2, 0, self.L - self.Lshear)
                self.mapdl.k(203, - self.bfi/2, 0, self.L - self.Lshear)
                self.mapdl.k(204, 0, self.bw, self.L - self.Lshear)
                self.mapdl.k(205, self.bfs/2, self.bw, self.L - self.Lshear)
                self.mapdl.k(206, - self.bfs/2, self.bw, self.L - self.Lshear)

                self.mapdl.k(301, 0, 0, self.L)
                self.mapdl.k(302, self.bfi/2, 0, self.L)
                self.mapdl.k(303, - self.bfi/2, 0, self.L)
                self.mapdl.k(304, 0, self.bw, self.L)
                self.mapdl.k(305, self.bfs/2, self.bw, self.L)
                self.mapdl.k(306, - self.bfs/2, self.bw, self.L)

                self.mapdl.a(1, 2, 102, 101)
                self.mapdl.a(1, 3, 103, 101)
                self.mapdl.a(4, 5, 105, 104)
                self.mapdl.a(4, 6, 106, 104)
                self.mapdl.a(1, 4, 104, 101)

                self.mapdl.a(101, 102, 202, 201)
                self.mapdl.a(101, 103, 203, 201)
                self.mapdl.a(104, 105, 205, 204)
                self.mapdl.a(104, 106, 206, 204)
                self.mapdl.a(101, 104, 204, 201)

                self.mapdl.a(201, 202, 302, 301)
                self.mapdl.a(201, 203, 303, 301)
                self.mapdl.a(204, 205, 305, 304)
                self.mapdl.a(204, 206, 306, 304)
                self.mapdl.a(201, 204, 304, 301)
        else:
            self.mapdl.k(1, 0, 0, 0)
            self.mapdl.k(2, self.bfi/2, 0, 0)
            self.mapdl.k(3, - self.bfi/2, 0, 0)
            self.mapdl.k(4, 0, self.bw, 0)
            self.mapdl.k(5, self.bfs/2, self.bw, 0)
            self.mapdl.k(6, - self.bfs/2, self.bw, 0)

            self.mapdl.k(101, 0, 0, self.L)
            self.mapdl.k(102, self.bfi/2, 0, self.L)
            self.mapdl.k(103, - self.bfi/2, 0, self.L)
            self.mapdl.k(104, 0, self.bw, self.L)
            self.mapdl.k(105, self.bfs/2, self.bw, self.L)
            self.mapdl.k(106, - self.bfs/2, self.bw, self.L)

            self.mapdl.a(1, 2, 102, 101)
            self.mapdl.a(1, 3, 103, 101)
            self.mapdl.a(4, 5, 105, 104)
            self.mapdl.a(4, 6, 106, 104)
            self.mapdl.a(1, 4, 104, 101)

