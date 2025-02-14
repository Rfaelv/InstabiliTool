import psutil
for process in (process for process in psutil.process_iter() if process.name()=="ANSYS.exe"):
    process.kill()