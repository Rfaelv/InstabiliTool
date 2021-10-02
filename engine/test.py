# import pyvista
# pyvista.Report(gpu=True)

# import psutil,os
# import psutil,os
# for process in (process for process in psutil.process_iter() if process.name()=="ANSYS.exe"):
#     # print(process)
#     process.kill()

# for process in psutil.process_iter():
#     print(process.name())
    # if process.name()=="ANSYS.exe"):
    # print(pid)
    # ansyscl.exe


from ansys.mapdl.core import launch_mapdl
import sys

pathToLaunch = 'D:\\Documentos\\Python\\PROJETOS\\GUI com Electron\\analise-de-flambagem-no-ansys\\data'

# mapdl = launch_mapdl(run_location = pathToLaunch, override=True,  cleanup_on_exit=True)
mapdl = launch_mapdl(run_location = pathToLaunch, override=True,  cleanup_on_exit=True, start_instance=False, clear_on_connect=False, remove_temp_files=True)
# help(launch_mapdl)
# mapdl.exit()
mapdl.prep7()
# mapdl.l(1,2)
# mapdl.k(1,0,0,1)
# mapdl.k(2,0,2,2)
mapdl.open_gui()
sys.exit()