# BCC unit cell with structured mesh in ABAQUS
author = "Sina Taghizadeh"
license = "GNU GPL Version 3.0"

from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models.changeKey(fromName='Model-1', toName='MyModel-1')
mdb.models['MyModel-1'].ConstrainedSketch(name='__sweep__', sheetSize=20.0)
mdb.models['MyModel-1'].sketches['__sweep__'].Line(point1=(0.0, 0.0), point2=(
    7.07106781186548, 5.0))
mdb.models['MyModel-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0, 
    transform=(0.577350269189626, -0.816496580927726, 0.0, -0.0, 0.0, 1.0, 
    -0.816496580927726, -0.577350269189626, -0.0, 0.0, 0.0, 0.0))
mdb.models['MyModel-1'].sketches['__profile__'].ConstructionLine(point1=(-10.0, 
    0.0), point2=(10.0, 0.0))
mdb.models['MyModel-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -10.0), point2=(0.0, 10.0))
mdb.models['MyModel-1'].sketches['__profile__'].CircleByCenterPerimeter(center=
    (0.0, 0.0), point1=(0.0, 0.5))
mdb.models['MyModel-1'].Part(dimensionality=THREE_D, name='Strut+', type=
    DEFORMABLE_BODY)
mdb.models['MyModel-1'].parts['Strut+'].BaseSolidSweep(path=
    mdb.models['MyModel-1'].sketches['__sweep__'], sketch=
    mdb.models['MyModel-1'].sketches['__profile__'])
del mdb.models['MyModel-1'].sketches['__profile__']
del mdb.models['MyModel-1'].sketches['__sweep__']
mdb.models['MyModel-1'].ConstrainedSketch(name='__sweep__', sheetSize=20.0)
mdb.models['MyModel-1'].sketches['__sweep__'].Line(point1=(7.07106781186548, 
    0.0), point2=(0.0, 5.0))
mdb.models['MyModel-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0, 
    transform=(0.577350269189626, 0.816496580927726, -0.0, 0.0, 0.0, 1.0, 
    0.816496580927726, -0.577350269189626, 0.0, 7.07106781186548, 0.0, 0.0))
mdb.models['MyModel-1'].sketches['__profile__'].ConstructionLine(point1=(-10.0, 
    0.0), point2=(10.0, 0.0))
mdb.models['MyModel-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -10.0), point2=(0.0, 10.0))
mdb.models['MyModel-1'].sketches['__profile__'].CircleByCenterPerimeter(center=
    (0.0, 0.0), point1=(0.0, 0.5))
mdb.models['MyModel-1'].Part(dimensionality=THREE_D, name='Strut-', type=
    DEFORMABLE_BODY)
mdb.models['MyModel-1'].parts['Strut-'].BaseSolidSweep(path=
    mdb.models['MyModel-1'].sketches['__sweep__'], sketch=
    mdb.models['MyModel-1'].sketches['__profile__'])
del mdb.models['MyModel-1'].sketches['__profile__']
del mdb.models['MyModel-1'].sketches['__sweep__']
mdb.models['MyModel-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['MyModel-1'].rootAssembly.Instance(dependent=ON, name='Strut+-1', 
    part=mdb.models['MyModel-1'].parts['Strut+'])
mdb.models['MyModel-1'].rootAssembly.Instance(dependent=ON, name='Strut--1', 
    part=mdb.models['MyModel-1'].parts['Strut-'])
mdb.models['MyModel-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['MyModel-1'].rootAssembly.instances['Strut+-1'], 
    mdb.models['MyModel-1'].rootAssembly.instances['Strut--1']), name='HalfUC', 
    originalInstances=SUPPRESS)
mdb.models['MyModel-1'].rootAssembly.Instance(dependent=ON, name='HalfUC-2', 
    part=mdb.models['MyModel-1'].parts['HalfUC'])
mdb.models['MyModel-1'].rootAssembly.DatumAxisByTwoPoint(point1=
    mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-2'].InterestingPoint(
    mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-2'].edges[4], 
    MIDDLE), point2=
    mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-2'].InterestingPoint(
    mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-2'].edges[0], 
    MIDDLE))
mdb.models['MyModel-1'].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 
    -10.0, 0.0), axisPoint=(3.535534, 2.5, 0.0), instanceList=('HalfUC-2', ))
mdb.models['MyModel-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-1'], 
    mdb.models['MyModel-1'].rootAssembly.instances['HalfUC-2']), name='BCCUC', 
    originalInstances=SUPPRESS)
mdb.models['MyModel-1'].rootAssembly.features['Datum axis-1'].resume()
mdb.models['MyModel-1'].rootAssembly.features['Datum axis-1'].suppress()
mdb.models['MyModel-1'].rootAssembly.features['HalfUC-2'].suppress()
mdb.models['MyModel-1'].parts['BCCUC'].DatumAxisByTwoPoint(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[2])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByTwoPoint(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[3], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5])
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=0.68, name='__profile__', 
    sheetSize=27.58, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[3], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(3.535534, 2.5, 0.0)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[3], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=0.68, name='__profile__', 
    sheetSize=27.58, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[3], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(3.535534, 2.5, 0.0)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=ON, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[3], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByRotation(angle=90.0, axis=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2], isDependent=False, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[3])
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=0.68, name='__profile__', 
    sheetSize=27.48, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[6], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(3.535534, 2.5, 0.0)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[6], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=0.66, name='__profile__', 
    sheetSize=26.43, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[6], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(3.535534, 2.5, 0.0)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(5.0, 5.0), 
    point2=(-5.0, -5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=ON, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[6], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[29], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[11])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-3']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[28], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[29], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[27], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[29], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[37], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[29], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[49], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[10])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[12])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[11])
mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[16], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[65], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[18], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[109], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[17])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[16])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[67], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[10], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[0], MIDDLE))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#3ffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[20])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-6']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-8']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-5']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-4']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-7']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-6']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-3']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-2']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Partition cell-1']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-5']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-4']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-3']
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=0.65, name='__profile__', 
    sheetSize=26.05, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].faces[30], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].edges[35], 
    sketchOrientation=RIGHT, origin=(3.535534, 5.0, 3.058069)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
del mdb.models['MyModel-1'].sketches['__profile__']

mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].rootAssembly.DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].rootAssembly.instances['BCCUC-1'].vertices[29], 
    point2=
    mdb.models['MyModel-1'].rootAssembly.instances['BCCUC-1'].vertices[8], 
    point3=
    mdb.models['MyModel-1'].rootAssembly.instances['BCCUC-1'].vertices[1])
del mdb.models['MyModel-1'].rootAssembly.features['Datum plane-1']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Cut extrude-4']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Cut extrude-3']
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-2']
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-1', 
    'Cut extrude-2', 'Cut extrude-1'))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByTwoPoint(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[3], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByOffset(flip=SIDE1, 
    isDependent=False, offset=3.0, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[22])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-2']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByOffset(flip=SIDE1, 
    isDependent=False, offset=5.0, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[22])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByRotation(angle=90.0, axis=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2], isDependent=False, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[22])
mdb.models['MyModel-1'].parts['BCCUC'].DatumAxisByTwoPoint(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[3])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByRotation(angle=90.0, axis=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[26], isDependent=False, 
    plane=mdb.models['MyModel-1'].parts['BCCUC'].datums[25])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByOffset(flip=SIDE1, 
    isDependent=False, offset=5.0, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[25])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByOffset(flip=SIDE1, 
    isDependent=False, offset=5.0, plane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[27])
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=1.07, name='__profile__', 
    sheetSize=43.07, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[24], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(0.0, 2.5, -3.535534)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[24], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=1.07, name='__profile__', 
    sheetSize=43.07, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[28], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[2], 
    sketchOrientation=RIGHT, origin=(7.071068, 2.5, -3.535534)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[28], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[2])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].ConstrainedSketch(gridSpacing=1.06, name='__profile__', 
    sheetSize=42.47, transform=
    mdb.models['MyModel-1'].parts['BCCUC'].MakeSketchTransform(
    sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[29], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['MyModel-1'].parts['BCCUC'].datums[26], 
    sketchOrientation=RIGHT, origin=(3.535534, 7.5, 0.0)))
mdb.models['MyModel-1'].parts['BCCUC'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['MyModel-1'].sketches['__profile__'])
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-2.5, -2.5), 
    point2=(2.5, 2.5))
mdb.models['MyModel-1'].sketches['__profile__'].rectangle(point1=(-5.0, -5.0), 
    point2=(5.0, 5.0))
mdb.models['MyModel-1'].parts['BCCUC'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['MyModel-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[29], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[26])
del mdb.models['MyModel-1'].sketches['__profile__']
mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[6], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[32], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[49], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[8], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[35])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[34])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[33])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[43], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[53], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[96], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[50], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[43], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[96], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[40])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[39])
mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-3'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-2'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-1'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-10', 
    'Partition cell-5'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-11', 
    'Partition cell-4'))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[9], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[49], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[15])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[27], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[37])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-8']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[13], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[21])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[35], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[36])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[46])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[45])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[43])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[59], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[56])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[58], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[60])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#ff ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[50])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#3fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[51])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[59], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[24])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[54])
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-3', 'Datum plane-12', 'Partition cell-6', 'Datum plane-11', 
    'Partition cell-5', 'Datum plane-10', 'Partition cell-4'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-2'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-1'))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByLinePoint(line=
    mdb.models['MyModel-1'].parts['BCCUC'].edges[6], point=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByLinePoint(line=
    mdb.models['MyModel-1'].parts['BCCUC'].edges[58], point=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByLinePoint(line=
    mdb.models['MyModel-1'].parts['BCCUC'].edges[7], point=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[56])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[57])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[58])
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-1'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-2'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-3'))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[36])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[19])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[7], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[18])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[63])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[62])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[64])
mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[112], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[26])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[9], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[112], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[18])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[69])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[68])
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-2'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-1'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-3'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-10', 
    'Partition cell-5'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-11', 
    'Partition cell-4'))

mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[23], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[23], MIDDLE), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[21])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-7']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[21], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[4])
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-7']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[14], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[41], MIDDLE), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[23])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[14], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[24], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[11])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[14], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[34], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[20])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[74])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[76])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[75])
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-1'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-3'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-2'))


mdb.models['MyModel-1'].rootAssembly.regenerate()
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), point1=mdb.models['MyModel-1'].parts['BCCUC'].vertices[26], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[31], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#3 ]', 
    ), ), point1=mdb.models['MyModel-1'].parts['BCCUC'].vertices[2], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[28], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[50], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#f ]', 
    ), ), point1=mdb.models['MyModel-1'].parts['BCCUC'].vertices[3], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[5], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[51], CENTER))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[13], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[12])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[34], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[11], MIDDLE), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[8])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[15], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[23])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#ff ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[83])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[85])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#3ffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[84])
mdb.models['MyModel-1'].parts['BCCUC'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.43)
mdb.models['MyModel-1'].parts['BCCUC'].generateMesh()
mdb.models['MyModel-1'].parts['BCCUC'].deleteMesh()
mdb.models['MyModel-1'].parts['BCCUC'].deleteSeeds()
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[55], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[1], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[14])
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-7', 
    'Partition cell-4'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-8', 
    'Partition cell-6'))
mdb.models['MyModel-1'].parts['BCCUC'].deleteFeatures(('Datum plane-9', 
    'Partition cell-5'))
del mdb.models['MyModel-1'].parts['BCCUC'].features['Datum plane-10']
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[35], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[4], MIDDLE), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[31])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[29], point2=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[9], MIDDLE), point3=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[25])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[51], MIDDLE), point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[3], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[47], MIDDLE))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask(('[#ff ]', 
    ), ), datumPlane=mdb.models['MyModel-1'].parts['BCCUC'].datums[93])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#fff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[92])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#3ffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[94])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[121], MIDDLE), point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[6], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[106], MIDDLE))
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[69], MIDDLE), point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[27], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[43], MIDDLE))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#ffffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[98])
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#ffffffff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[99])
mdb.models['MyModel-1'].parts['BCCUC'].DatumPlaneByThreePoints(point1=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[81], MIDDLE), point2=
    mdb.models['MyModel-1'].parts['BCCUC'].vertices[34], point3=
    mdb.models['MyModel-1'].parts['BCCUC'].InterestingPoint(
    mdb.models['MyModel-1'].parts['BCCUC'].edges[170], MIDDLE))
mdb.models['MyModel-1'].parts['BCCUC'].PartitionCellByDatumPlane(cells=
    mdb.models['MyModel-1'].parts['BCCUC'].cells.getSequenceFromMask((
    '[#ffffffff #ff ]', ), ), datumPlane=
    mdb.models['MyModel-1'].parts['BCCUC'].datums[102])
mdb.models['MyModel-1'].parts['BCCUC'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.2)
mdb.models['MyModel-1'].parts['BCCUC'].generateMesh()


