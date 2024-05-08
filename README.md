# Abaqus_BCC_UnitCell
BCC unit cell with structured mesh in ABAQUS

# Description:

Lattice materials constructed with BCC unit cells are among the most popular lattice materials or structures in engineering. Different dimensions of these BCC lattice structures are shown in the figure below.

<img width="700" alt="t1" src="https://github.com/Sina-Taghizadeh/Abaqus_BCC_UnitCell/assets/162900845/59ae7570-f236-4451-8842-e30226199b60">

For FEM analysis of these structures, we need their geometric model in a CAD software and meshing of the geometry. The CAD model of this BCC unit cell, due to its relatively complex shape, only allows the use of tetrahedral elements. In Abaqus, if we want to use hexahedral elements for their analysis, we need to define a relatively large number of partitions. In this project, I have created the CAD model of this unit cell along with its partitions in such a way that the final geometry is shown in green in the figure below.

<img width="300" alt="t1" src="https://github.com/Sina-Taghizadeh/Abaqus_BCC_UnitCell/assets/162900845/8968c53b-46de-4254-9759-d1b66118e25e">

# How to use:

**1) Run Abaqus.**

**2) Click on the "Run Script" option from the "File" tab.**

**3) Select the BCCUC.py code available in the repo.**

# Collaboration:

This code can be modularized and developed to automatically make changes and generate a new model for different radii of the unit cell struts. I would be happy if someone implemented these changes and extended the current project.

sina.taghizadeh123@gmail.com

