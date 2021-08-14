# import pyvista
# pyvista.Report(gpu=True)

# import psutil,os
import psutil,os
for process in (process for process in psutil.process_iter() if process.name()=="ANSYS.exe"):
    # print(process)
    process.kill()

# for process in psutil.process_iter():
#     print(process.name())
    # if process.name()=="ANSYS.exe"):
    # print(pid)
    # ansyscl.exe