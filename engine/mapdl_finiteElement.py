class FiniteElement():
    def __init__(self, mapdl):
        self.mapdl = mapdl

    def createShell181(self):
        self.mapdl.run("/PREP7")
        self.mapdl.et(1, "SHELL181")
        self.mapdl.keyopt(1, 1, 0)
        self.mapdl.keyopt(1, 3, 2)
        self.mapdl.keyopt(1, 8, 0)
        self.mapdl.keyopt(1, 9, 0) 
        self.mapdl.keyopt(1, 10, 0)

        # setting defined local element axes
        self.mapdl.local(11, 0, 0, 0, 0, 0, 0, 0)
        self.mapdl.esys(11)
    
    def createCombin39(self, conectionStiffness):
        self.mapdl.et(2, 'COMBIN39')
        self.mapdl.keyopt(2, 1, 0)
        self.mapdl.keyopt(2, 2, 0)
        self.mapdl.keyopt(2, 3, 6)
        self.mapdl.keyopt(2, 4, 0)
        self.mapdl.keyopt(2, 6, 0)
        self.mapdl.r(2, -1, -conectionStiffness, 0, 0, 1, conectionStiffness) # Curve Force x rad
