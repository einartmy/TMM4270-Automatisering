from Shapes.Cylinder import Cylinder
from Shapes.Block_2 import Block_2
import NXOpen
import math

class Gear:

        def __init__(self, gearR, toothLength, toothWidth, gearHeight, x, y):
            self.gearR = gearR
            self.toothLength = toothLength
            self.toothWidth = toothWidth
            self.gearHeight = gearHeight
            self.x = x
            self.y = y
            
            
            teeth = math.ceil(math.pi*gearR // toothWidth*0.9)
            angle = 2*math.pi / (teeth)
            cylinder_radius = gearR
            gear = Cylinder(x,y,0, cylinder_radius * 2, gearHeight,  [0,0,1])
            for i in range(0, teeth):
                tooth = Block_2(x + (cylinder_radius-0.5*toothLength)*math.cos(i*angle),
                    y + (cylinder_radius-0.5*toothLength)*math.sin(i*angle),
                    0,
                    toothLength,
                    toothWidth,
                    gearHeight,
                    NXOpen.Vector3d(math.cos((i+15/gearR)*angle),              math.sin((i+15/gearR)*angle),              0.0),
                    NXOpen.Vector3d(math.cos((i+15/gearR)*angle +math.pi/2),   math.sin((i+15/gearR)*angle +math.pi/2),   0.0))
                gear.unite(tooth)
            hole_in_gear = Cylinder(x, y, 0, cylinder_radius/15, gearHeight,[0,0,1])
            gear.subtract(hole_in_gear)
            
            
	
    # def __init__(self, gearR, toothLength, toothWidth, gearHeight, x, y):
    #     self.gearR = gearR
    #     self.toothLength = toothLength
    #     self.toothWidth = toothWidth
    #     self.gearHeight = gearHeight
    #     self.x = x
    #     self.y = y
        
        
    #     teeth = math.ceil(math.pi*gearR // toothWidth*0.9)
    #     angle = 2*math.pi / (teeth)
    #     cylinder_radius = gearR-toothLength
    #     gear = Cylinder(x,y,0, cylinder_radius * 2, gearHeight,  [0,0,1])
    #     for i in range(0, teeth):
    #         tooth = Block_2(x + (cylinder_radius-0.1*toothLength)*math.cos(i*angle),
    #             y + (cylinder_radius-0.1*toothLength)*math.sin(i*angle),
    #             0,
    #             toothLength,
    #             toothWidth,
    #             gearHeight,
    #             NXOpen.Vector3d(math.cos((i+15/gearR)*angle),              math.sin((i+15/gearR)*angle),              0.0),
    #             NXOpen.Vector3d(math.cos((i+15/gearR)*angle +math.pi/2),   math.sin((i+15/gearR)*angle +math.pi/2),   0.0))
    #         gear.unite(tooth)
    #     hole_in_gear = Cylinder(x, y, 0, cylinder_radius/15, gearHeight,[0,0,1])
    #     gear.subtract(hole_in_gear)
            