from Shapes.Cylinder import Cylinder
from Shapes.Block import Block

class upperCase:

    def __init__(self, gearRadius, gearDepth, toothradius, thickness, x, y):
        self.gearRadius = gearRadius
        self.toothradius = toothradius
        self.outerRadius = gearRadius + toothradius + thickness
        self.depth = gearDepth                                          #Depth inside the case, same as gear depth
        self.thickness = thickness                                     #Thickness of case
        self.x = x
        self.y = y

        self.initForNX()

    def initForNX(self):
        
        mainCylinder = Cylinder(self.x, self.y, -self.thickness, self.outerRadius * 2, self.depth + 2*self.thickness)

        subtractCylinder = Cylinder(self.x, self.y, 0, self.outerRadius * 2 - 2*self.thickness, self.depth)

        mainCylinder.subtract(subtractCylinder)

        mainBlock = Block(self.x - 2* self.outerRadius, self.y-self.gearRadius - self.toothradius, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height )

        subtractBlock = Block(self.x - 2* self.outerRadius, self.y -self.gearRadius - self.toothradius, mainCylinder.z + self.thickness,
                               4*self.outerRadius, self.gearRadius - self.thickness, mainCylinder.height - 2*self.thickness)

        mainBlock.subtract(subtractBlock)

        subtractCylinder = Cylinder(self.x, self.y, 0, self.outerRadius * 2 - 2*self.thickness, self.depth)
        
        mainBlock.subtract(subtractCylinder)

        mainCylinder.unite(mainBlock)

        subtractBlock = Block(self.x - 2* self.outerRadius, self.y-self.gearRadius*2 - self.toothradius, mainCylinder.z + self.thickness,
                               4*self.outerRadius, self.gearRadius*2 - self.thickness, mainCylinder.height - 2*self.thickness)

        mainCylinder.subtract(subtractBlock)

