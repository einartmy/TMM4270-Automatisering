import sys

#----------------CHANGE TO YOUR PATH
sys.path.append('M:\Desktop\TMM4270\KBE\Python')
#-----------------------------------

from Shapes.Block import Block
from Shapes.Cylinder import Cylinder
from Shapes.Sphere import Sphere
from Shapes.Cone import Cone

block = Block(200, 0, -150, 100, 100, 100)

cylinder = Cylinder(200, 0, 50, 10, 50)

sphere = Sphere(200, 0, 0, 100)

cone = Cone(200, 0, 60, 90, 25, 60)

