[Home](./)  |  [About](./about.html)  |  [Documentation](./documentation.html) 
Welcome to the Instabilitool documentation! If this is your first time exploring the InstabiliTool app, read through this section to get familiar with the basics. Appreciate it.

## Prerequisites

To use this app, you need to have a local installation of Ansys. The version of Ansys installed will dictate the interface and features available to you.
Visit [Ansys](https://www.ansys.com/) for more information on getting a licensed copy of Ansys.

### ANSYS Software Requirements
For the latest features, you will need a copy of ANSYS 2021R1 installed locally, but this app is compatible with ANSYS 17.0 and newer.

### Verifying Your Installation
The InstabiliTool app always will automatically verify your Ansys instalation in the initialization. If there is an problem with the Ansys instalation path, it will promp an window to the user insert the Ansys binary path.

## Analysi preferences


## Analysi type

InstabiliTool allows to perform linear and non-linear instability analysi. In the linear one is used the Eigen Buckling type of analysi of the Ansys. In contrast, the non-linear analysi use the static analysi of the Ansys with an step-load sequency process (geometric nonlinearity).

## Material properties

This program provide isotropic, orthotropic and anisotropic material models possibilities. However, only linear material are allowed.

## Geometry

It was choosed the most common sections to offer in this app. They are: I, Tubular, C, C whit stiffeners, Rack, Angle and Plate.

## Mesh and material assignment

The mesh can be triangular or rectangular and is allowed the maped and free methods of generation.

## Load

The load can be normal or bending moment. To the normal load is allowed the point in the centroid or an distributed load along the whole cross section. With the point load at the centroid can be added a moment to represent eccentricity.
In other hands, to the bending moment load is alloed trhee-points bending or four-points bending model.

## Boundary conditions

It is possible to apply boundary condition to any cross section in th eextension of the profile (The range of cross sections is as large as is the discretization applaied in the meshing step).

## Script generator

For the more explorative users, it is disponibilized the Python and/or MAPDL script of the analysi created with the GUI. This can be interesting for those who want to explore features that are not included in the InstabiliTool.

## Support or Contact

Having trouble with InstabiliTool? Contact us [here](malito:ravieira@id.uff.br?subject=Help me with InstabiliTool).
