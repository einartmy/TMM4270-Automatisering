from Shapes.Cylinder import Cylinder
from Shapes.Block_2 import Block_2
import NXOpen
import math

class Gear:
	
    def __init__(self, gearR, toothL, gearHeight, x, y):
        self.gearR = gearR
        self.toothL = toothL
        self.gearHeight = gearHeight
        self.x = x
        self.y = y
        
        teeth = math.floor(gearR / 6)
        angle = 2*math.pi / teeth
        cylinder_radius = gearR-toothL
        gear = Cylinder(x,y,0, cylinder_radius * 2, gearHeight,  [0,0,1])
        for i in range(0, teeth):
            tooth = Block_2(x + (cylinder_radius-0.1*toothL)*math.cos(i*angle),
                y + (cylinder_radius-0.1*toothL)*math.sin(i*angle),
                0,
                toothL,
                toothL,
                gearHeight,
                NXOpen.Vector3d(math.cos(i*angle), math.sin(i*angle), 0.0),
                NXOpen.Vector3d(math.cos(i*angle+math.pi/2), math.sin(i*angle+math.pi/2),0.0))
            gear.unite(tooth)
        hole_in_gear = Cylinder(x, y, 0, cylinder_radius/15, gearHeight,[0,0,1])
        gear.subtract(hole_in_gear)
            