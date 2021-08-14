class FiniteElement():
    def createShell181(self, mapdl):
        mapdl.et(1, "SHELL181")
        mapdl.keyopt(1, 1, 0)
        mapdl.keyopt(1, 3, 2)
        mapdl.keyopt(1, 8, 0)
        mapdl.keyopt(1, 9, 0) 
        mapdl.keyopt(1, 10, 0)

        # setting defined local element axes
        mapdl.local(11, 0, 0, 0, 0, 0, 0, 0)
        mapdl.esys(11)