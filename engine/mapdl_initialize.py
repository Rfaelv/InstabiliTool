from ansys.mapdl.core import launch_mapdl


class MapdlInitialize:
    def __init__(self):
        self.mapdl = launch_mapdl()
        print(self.mapdl)
    def getInstance(self):
        return self.mapdl