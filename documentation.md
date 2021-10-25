[Home](./)  |  [About](./about.html)  |  [Documentation](./documentation.html) 

Welcome to the Instabilitool documentation! If this is your first time exploring the InstabiliTool app, read through this section to get familiar with the basics. Appreciate it.

## Requirements

To use this app, you need to have a local installation of Ansys. The version of Ansys installed will dictate the interface and features available to you.
Visit [Ansys](https://www.ansys.com/) for more information on getting a licensed copy of Ansys.

#### ANSYS Software Requirements
For the latest features, you will need a copy of ANSYS 2021R1 installed locally, but this app is compatible with ANSYS 17.0 and newer.

#### Verifying Your Installation
The InstabiliTool app always will automatically verify your Ansys installation in the initialization. If there is a problem with the Ansys installation path, it will prompt a window to the user insert the Ansys binary path.

## Analysis preferences
### General analysis
`Asnsy binary path`: If the Ansys binary path is not in the default directory, must be defined.

`Connections type`: The connections bettwen flange and web geometrys can be `rigid` or `flexible`. In case of flexible, you need to inform the `Conection stiffness`.

`Connection stiffness`: Stiffness value that will be used for the all flange-web connection in the model. 

Shell 181 properties:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Element stiffness`: (default: 0).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Integration option`: (default: 2).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Curved shell formulation`: (default: 0).

### Linear analysis
`Mode number`: Number of modes to extract (default: 10).

### Non-linear anlysis
`Load factor`: The critical load of linear analysis is updated with this factor to be applied in nonlinear analysis (default: 1.2).
`Initial deformation factor`: This factor will be applied to the minor tickness of the profile and the result will be applied to the buckling deformation resulting in linear analysis (default: 0.1).
`Steps`: Number of steps used in the analysis (default: 100)

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
