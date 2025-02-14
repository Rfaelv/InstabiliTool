import os
from ansys.mapdl.core import launch_mapdl
import time
# path = os.getcwd() + '//engine//linearAnalysi//ansysData'
path = os.getcwd() + '//ansysData'
mapdl = launch_mapdl(run_location=path, loglevel='ERROR')

mapdl.finish()
mapdl.clear()
mapdl.run('/FILNAME,VigaI,0')
# mapdl.run(f'/CWD, {path}')

mapdl.prep7()


# 1 - Geometria:

# mapdl.run("t=0.00635")

# mapdl.run("bf=0.1524")

# mapdl.run("d=0.1524")

# mapdl.run("bw=d-t")

# # L=2.9

# # L=2.6

# # L=2.2

# mapdl.run("L=1.8")

# # Lshear=1

# # Lshear=0.9

# # Lshear=0.8

# mapdl.run("Lshear=0.7")

# # 2 - Propriedades do material:

# # mesa

# mapdl.run("Ex1=9444000000")

# # Compressão

# # Ey1=31219000000

# # Flexão

# mapdl.run("Ey1=18750000000")

# mapdl.run("Ez1=9444000000")

# mapdl.run("PRxy1=0.32")

# mapdl.run("PRyz1=0.16")

# mapdl.run("PRxz1=0.16")

# mapdl.run("Gxy1=2882000000")

# mapdl.run("Gyz1=2882000000")

# mapdl.run("Gxz1=2882000000")

# mapdl.run("Dens1=1800")

# # alma

# mapdl.run("Ex2=8289000000")

# # Compressão

# # Ey2=31250000000

# # Flexão

# mapdl.run("Ey2=18750000000")

# mapdl.run("Ez2=8289000000")

# mapdl.run("PRxy2=0.32")

# mapdl.run("PRyz2=0.16")

# mapdl.run("PRxz2=0.16")

# mapdl.run("Gxy2=2882000000")

# mapdl.run("Gyz2=2882000000")

# mapdl.run("Gxz2=2882000000")

# mapdl.run("Dens2=1800")

# # =======  PRE-PROCESSAMENTO  =======

# # -------  INICIALIZACAO DA FASE DE PRE-PROCESSAMENTO  -------

# mapdl.run("/PREP7")

# mapdl.run("/VIEW,1,1,1,1")

# mapdl.run("/TITLE,Viga I - Secao: %d*1000% x %bf*1000% - Comprimento: %L%m")

# mapdl.run("/REPLOT")

# # BCSOPTION,,DEFAULT

# # -------  CRIACAO DO ELEMENTO FINITO  -------

# mapdl.et(1, "SHELL181")

# mapdl.keyopt(1, 1, 0)  #Element stiffness: 0 - Bending and membrane stiffness (default)

# mapdl.keyopt(1, 3, 2)  #Integration option: 2 - Full integration with incompatible modes

# mapdl.keyopt(1, 8, 0)  #Specify layer data storage: 0 - Store data for bottom of bottom layer and top of top layer (multi-layer elements) (default)

# mapdl.keyopt(1, 9, 0)  #User thickness option: 0 - No user subroutine to provide initial thickness (default)

# mapdl.keyopt(1, 10, 0)  #Curved shell formulation: 0 - Standard shell formulation (default)

# mapdl.et(2, "SHELL181")

# mapdl.keyopt(2, 1, 0)  #Element stiffness: 0 - Bending and membrane stiffness (default)

# mapdl.keyopt(2, 3, 2)  #Integration option: 2 - Full integration with incompatible modes

# mapdl.keyopt(2, 8, 0)  #Specify layer data storage: 0 - Store data for bottom of bottom layer and top of top layer (multi-layer elements) (default)

# mapdl.keyopt(2, 9, 0)  #User thickness option: 0 - No user subroutine to provide initial thickness (default)

# mapdl.keyopt(2, 10, 0)  #Curved shell formulation: 0 - Standard shell formulation (default)

# # -------  CRIACAO DO MATERIAL  -------

# mapdl.mp("EX", 1, "Ex1")

# mapdl.mp("EY", 1, "Ey1")

# mapdl.mp("EZ", 1, "Ez1")

# mapdl.mp("PRXY", 1, "PRxy1")

# mapdl.mp("PRXZ", 1, "PRxz1")

# mapdl.mp("PRYZ", 1, "PRyz1")

# mapdl.mp("GXY", 1, "Gxy1")

# mapdl.mp("GXZ", 1, "Gxz1")

# mapdl.mp("GYZ", 1, "Gyz1")

# mapdl.mp("DENS", 1, "Dens1")

# mapdl.mp("EX", 2, "Ex2")

# mapdl.mp("EY", 2, "Ey2")

# mapdl.mp("EZ", 2, "Ez2")

# mapdl.mp("PRXY", 2, "PRxy2")

# mapdl.mp("PRXZ", 2, "PRxz2")

# mapdl.mp("PRYZ", 2, "PRyz2")

# mapdl.mp("GXY", 2, "Gxy2")

# mapdl.mp("GXZ", 2, "Gxz2")

# mapdl.mp("GYZ", 2, "Gyz2")

# mapdl.mp("DENS", 2, "Dens2")

# # -------  CRIACAO DA SECAO  -------

# mapdl.sectype(1, "SHELL", "", "mesa")

# mapdl.secoffset("MID")

# mapdl.secdata("t", 1)

# mapdl.sectype(2, "SHELL", "", "alma")

# mapdl.secoffset("MID")

# mapdl.secdata("t", 2)

# # -------  LOCACAO DOS KEYPOINTS  -------

# mapdl.k(1, 0, 0, 0)

# mapdl.k(2, "bf/2", 0, 0)

# mapdl.k(3, "bf", 0, 0)

# mapdl.k(4, 0, "bw", 0)

# mapdl.k(5, "bf/2", "bw", 0)

# mapdl.k(6, "bf", "bw", 0)

# mapdl.k(101, 0, 0, "Lshear")

# mapdl.k(102, "bf/2", 0, "Lshear")

# mapdl.k(103, "bf", 0, "Lshear")

# mapdl.k(104, 0, "bw", "Lshear")

# mapdl.k(105, "bf/2", "bw", "Lshear")

# mapdl.k(106, "bf", "bw", "Lshear")

# mapdl.k(201, 0, 0, "L-Lshear")

# mapdl.k(202, "bf/2", 0, "L-Lshear")

# mapdl.k(203, "bf", 0, "L-Lshear")

# mapdl.k(204, 0, "bw", "L-Lshear")

# mapdl.k(205, "bf/2", "bw", "L-Lshear")

# mapdl.k(206, "bf", "bw", "L-Lshear")

# mapdl.k(301, 0, 0, "L")

# mapdl.k(302, "bf/2", 0, "L")

# mapdl.k(303, "bf", 0, "L")

# mapdl.k(304, 0, "bw", "L")

# mapdl.k(305, "bf/2", "bw", "L")

# mapdl.k(306, "bf", "bw", "L")

# # -------  CRIACAO DAS AREAS  -------

# mapdl.a(1, 2, 102, 101)

# mapdl.a(2, 3, 103, 102)

# mapdl.a(4, 5, 105, 104)

# mapdl.a(5, 6, 106, 105)

# mapdl.a(2, 5, 105, 102)

# mapdl.a(101, 102, 202, 201)

# mapdl.a(102, 103, 203, 202)

# mapdl.a(104, 105, 205, 204)

# mapdl.a(105, 106, 206, 205)

# mapdl.a(102, 105, 205, 202)

# mapdl.a(201, 202, 302, 301)

# mapdl.a(202, 203, 303, 302)

# mapdl.a(204, 205, 305, 304)

# mapdl.a(205, 206, 306, 305)

# mapdl.a(202, 205, 305, 302)

# # -------  GERACAO DE ELEMENTO E MALHA  -------

# mapdl.asel("ALL")

# mapdl.asel("S", "LOC", "Y", 0)

# mapdl.asel("A", "LOC", "Y", "bw")

# mapdl.aatt(1, 1, 1, 0, 1)

# mapdl.asel("ALL")

# mapdl.asel("S", "LOC", "X", "bf/2")

# mapdl.aatt(2, 2, 2, 0, 2)

# mapdl.asel("ALL")

# mapdl.mshkey(1)

# mapdl.aesize("ALL", 0.01)

# mapdl.amesh("ALL")

# # -------  FINALIZACAO DA FASE DE PRE-PROCESSAMENTO -------

# mapdl.finish()

# # =======  PROCESSAMENTO  =======

# # -------  INICIALIZACAO DA FASE DE PROCESSAMENTO  -------

# mapdl.run("/SOLU")

# # -------  DEFINICAO DAS RESTRICOES DE GRAU DE LIBERDADE  -------

# mapdl.nsel("S", "LOC", "Z", 0)

# mapdl.nsel("R", "LOC", "X", 0, "bf")

# mapdl.nsel("R", "LOC", "Y", 0)

# mapdl.d("ALL", "UX", 0)

# mapdl.d("ALL", "UY", 0)

# mapdl.d("ALL", "UZ", 0)

# mapdl.nsel("S", "LOC", "Z", "L")

# mapdl.nsel("R", "LOC", "X", 0, "bf")

# mapdl.nsel("R", "LOC", "Y", 0)

# mapdl.d("ALL", "UX", 0)

# mapdl.d("ALL", "UY", 0)

# mapdl.nsel("S", "LOC", "Z", 0)

# mapdl.nsel("R", "LOC", "X", 0, "bf")

# mapdl.nsel("R", "LOC", "Y", "bw")

# mapdl.d("ALL", "UX", 0)

# mapdl.d("ALL", "ROTZ", 0)

# mapdl.nsel("S", "LOC", "Z", "L")

# mapdl.nsel("R", "LOC", "X", 0, "bf")

# mapdl.nsel("R", "LOC", "Y", "bw")

# mapdl.d("ALL", "UX", 0)

# mapdl.d("ALL", "ROTZ", 0)

#------------------------------------------
t = 0.00635
bf = 0.1524
d = 0.1524
bw = d-t

L=1.8
Lshear=0.7

Ex1=9444000000
Ey1=18750000000
Ez1=9444000000
PRxy1=0.32
PRyz1=0.16
PRxz1=0.16
Gxy1=2882000000
Gyz1=2882000000
Gxz1=2882000000
Dens1=1800

Ex2=8289000000
Ey2=18750000000
Ez2=8289000000
PRxy2=0.32
PRyz2=0.16
PRxz2=0.16
Gxy2=2882000000
Gyz2=2882000000
Gxz2=2882000000
Dens2=1800

# ==============

mapdl.run("/PREP7")
mapdl.run("/VIEW,1,1,1,1")
mapdl.run("/TITLE,Viga I - Secao: %d*1000% x %bf*1000% - Comprimento: %L%m")
mapdl.run("/REPLOT")

mapdl.et(1, "SHELL181")
mapdl.keyopt(1, 1, 0)  
mapdl.keyopt(1, 3, 2)  
mapdl.keyopt(1, 8, 0)  
mapdl.keyopt(1, 9, 0)  
mapdl.keyopt(1, 10, 0) 

mapdl.et(2, "SHELL181")
mapdl.keyopt(2, 1, 0)  
mapdl.keyopt(2, 3, 2)  
mapdl.keyopt(2, 8, 0)  
mapdl.keyopt(2, 9, 0)  
mapdl.keyopt(2, 10, 0)  

mapdl.mp("EX", 1, Ex1)
mapdl.mp("EY", 1, Ey1)
mapdl.mp("EZ", 1, Ez1)
mapdl.mp("PRXY", 1, PRxy1)
mapdl.mp("PRXZ", 1, PRxz1)
mapdl.mp("PRYZ", 1, PRyz1)
mapdl.mp("GXY", 1, Gxy1)
mapdl.mp("GXZ", 1, Gxz1)
mapdl.mp("GYZ", 1, Gyz1)
mapdl.mp("DENS", 1, Dens1)

mapdl.mp("EX", 2, Ex2)
mapdl.mp("EY", 2, Ey2)
mapdl.mp("EZ", 2, Ez2)
mapdl.mp("PRXY", 2, PRxy2)
mapdl.mp("PRXZ", 2, PRxz2)
mapdl.mp("PRYZ", 2, PRyz2)
mapdl.mp("GXY", 2, Gxy2)
mapdl.mp("GXZ", 2, Gxz2)
mapdl.mp("GYZ", 2, Gyz2)
mapdl.mp("DENS", 2, Dens2)

mapdl.sectype(1, "SHELL", "", "mesa")
mapdl.secoffset("MID")
mapdl.secdata(t, 1)

mapdl.sectype(2, "SHELL", "", "alma")
mapdl.secoffset("MID")
mapdl.secdata(t, 2)

mapdl.k(1, 0, 0, 0)
mapdl.k(2, bf/2, 0, 0)
mapdl.k(3, bf, 0, 0)
mapdl.k(4, 0, bw, 0)
mapdl.k(5, bf/2, bw, 0)
mapdl.k(6, bf, bw, 0)
mapdl.k(101, 0, 0, Lshear)
mapdl.k(102, bf/2, 0, Lshear)
mapdl.k(103, bf, 0, Lshear)
mapdl.k(104, 0, bw, Lshear)
mapdl.k(105, bf/2, bw, Lshear)
mapdl.k(106, bf, bw, Lshear)
mapdl.k(201, 0, 0, L-Lshear)
mapdl.k(202, bf/2, 0, L-Lshear)
mapdl.k(203, bf, 0, L-Lshear)
mapdl.k(204, 0, bw, L-Lshear)
mapdl.k(205, bf/2, bw, L-Lshear)
mapdl.k(206, bf, bw, L-Lshear)
mapdl.k(301, 0, 0, L)
mapdl.k(302, bf/2, 0, L)
mapdl.k(303, bf, 0, L)
mapdl.k(304, 0, bw, L)
mapdl.k(305, bf/2, bw, L)
mapdl.k(306, bf, bw, L)

mapdl.a(1, 2, 102, 101)
mapdl.a(2, 3, 103, 102)
mapdl.a(4, 5, 105, 104)
mapdl.a(5, 6, 106, 105)
mapdl.a(2, 5, 105, 102)
mapdl.a(101, 102, 202, 201)
mapdl.a(102, 103, 203, 202)
mapdl.a(104, 105, 205, 204)
mapdl.a(105, 106, 206, 205)
mapdl.a(102, 105, 205, 202)
mapdl.a(201, 202, 302, 301)
mapdl.a(202, 203, 303, 302)
mapdl.a(204, 205, 305, 304)
mapdl.a(205, 206, 306, 305)
mapdl.a(202, 205, 305, 302)

mapdl.asel("ALL")
mapdl.asel("S", "LOC", "Y", 0)
mapdl.asel("A", "LOC", "Y", bw)
mapdl.aatt(1, 1, 1, 0, 1)
mapdl.asel("ALL")
mapdl.asel("S", "LOC", "X", bf/2)
mapdl.aatt(2, 2, 2, 0, 2)
mapdl.asel("ALL")
mapdl.mshkey(1)
mapdl.aesize("ALL", 0.01)
mapdl.amesh("ALL")
mapdl.finish()

mapdl.run("/SOLU")
mapdl.nsel("S", "LOC", "Z", 0)
mapdl.nsel("R", "LOC", "X", 0, bf)
mapdl.nsel("R", "LOC", "Y", 0)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "UY", 0)
mapdl.d("ALL", "UZ", 0)
mapdl.nsel("S", "LOC", "Z", L)
mapdl.nsel("R", "LOC", "X", 0, bf)
mapdl.nsel("R", "LOC", "Y", 0)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "UY", 0)
mapdl.nsel("S", "LOC", "Z", 0)
mapdl.nsel("R", "LOC", "X", 0, bf)
mapdl.nsel("R", "LOC", "Y", bw)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "ROTZ", 0)
mapdl.nsel("S", "LOC", "Z", L)
mapdl.nsel("R", "LOC", "X", 0, bf)
mapdl.nsel("R", "LOC", "Y", bw)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "ROTZ", 0)
#------------------------------------------

# NSEL,NONE

# -------  DEFINICAO DO CARREGAMENTO  -------

mapdl.fk(105, "FY", -1)

mapdl.fk(205, "FY", -1)

# -------  ANALISE ESTATICA  -------

mapdl.antype("STATIC")

mapdl.pstres("ON")

mapdl.allsel("ALL")

mapdl.solve()

mapdl.finish()

# -------  ANALISE DE ESTABILIDADE ELASTICA (FLAMBAGEM)  -------

mapdl.run("/SOLU")

mapdl.antype("BUCKLE")

mapdl.bucopt("LANB", 10)

mapdl.solve()

mapdl.finish()

mapdl.run("/SOLU")

mapdl.expass("ON")  #EXPASS: ESPECIFICA O PASSO DE EXPANS�O DE UMA AN�LISE (ON - UM PASSO DE EXPANS�O SER� REALIZADO)

mapdl.mxpand(10)  #MXPAND: ESPECIFICA O N�MERO DE MODOS PARA EXPANDIR E GRAVAR EM UMA AN�LISE MODAL OU DE FLAMBAGEM

mapdl.solve()

mapdl.finish()

# mapdl.vplot()
# mapdl.post1()
# mapdl.allsel()
# mapdl.set(1,5)
# mapdl.plnsol('U','SUM')
# mapdl.finish()


mapdl.run('/POST1')
mapdl.run('SUBSET,1,5')
mapdl.run('PLNSOL,U,SUM')
mapdl.run('/REPLOT')
mapdl.run('/SHOW,JPEG,,0')
mapdl.run('JPEG,QUAL,100')
mapdl.run('JPEG,ORIENT,HORIZ')
mapdl.run('JPEG,COLOR,2')
mapdl.run('JPEG,TMOD,1')	
mapdl.run('/GFILE,800,')	
mapdl.run('/REPLOT')
mapdl.run('/SHOW,CLOSE')
mapdl.run('/DEVICE,VECTOR,0')
mapdl.finish()

mapdl.exit()

