from abaqus import *
from abaqusConstants import *
import regionToolset

# Creating the Model
mdb.models.changeKey(fromName = 'Model-1', toName = 'Cantilever Beam')
beamModel = mdb.models['Cantilever Beam']

# Creating the Part
import sketch
import partition

beamProfileSketch = beamModel.ConstrainedSketch(name = 'Beam CS Profile', sheetSize = 5)
beamProfileSketch.rectangle(point1 = (0.1,0.1), point2 = (0.3, -0.1)


