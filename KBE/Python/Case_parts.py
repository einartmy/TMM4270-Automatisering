from Shapes.Cylinder import Cylinder
from Shapes.Block import Block

gearRadius  = 0
toothradius = 0 
outerRadius = 0 
depth       = 0                             
thickness   = 0                              
x           = 0
y           = 0

def getSubtractCylinder(self):
            return Cylinder(self.x, self.y, 0, (2*self.outerRadius) - (2*self.thickness) - self.toothradius, self.depth)

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
        xBlock = self.x - 2* self.outerRadius
        yBlock = self.y - self.gearRadius


        mainCylinder = Cylinder(self.x, self.y, -self.thickness, self.outerRadius * 2 - self.toothradius, self.depth + 2*self.thickness)
        mainBlock =     Block(xBlock, yBlock, mainCylinder.z ,                  4*self.outerRadius, self.gearRadius,                    mainCylinder.height )
        mainCylinder.unite(mainBlock)


        subtractCylinder = getSubtractCylinder(self)
        mainCylinder.subtract(subtractCylinder)

        


        
        subtractBlock = Block(xBlock, yBlock, mainCylinder.z + self.thickness,  4*self.outerRadius, self.gearRadius - self.thickness,   mainCylinder.height - 2*self.thickness)
        mainCylinder.subtract(subtractBlock)

        #subtractCylinder = getSubtractCylinder(self) 
        #mainBlock.subtract(subtractCylinder)

        

        #subtractBlock = Block(xBlock, yBlock*2, mainCylinder.z + self.thickness, 4*self.outerRadius, self.gearRadius*2 - self.thickness, mainCylinder.height - 2*self.thickness)

        #mainCylinder.subtract(subtractBlock)

        subtractBlock2 = Block(xBlock, yBlock*2, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height)

        mainCylinder.subtract(subtractBlock2) 




class lowerCase:

    def __init__(self, gearRadius, gearDepth, toothradius, thickness, x, y):
        self.gearRadius = gearRadius
        self.toothradius = toothradius
        self.outerRadius = gearRadius + toothradius + thickness
        self.depth = gearDepth                                          #Depth inside the case, same as gear depth
        self.thickness = thickness                                      #Thickness of case
        self.x = x
        self.y = y
        

        self.initForNX()

    def initForNX(self):
        xBlock = self.x - 2* self.outerRadius

        mainCylinder = Cylinder(self.x, self.y, -self.thickness, self.outerRadius * 2 - self.toothradius, self.depth + 2*self.thickness)

        subtractCylinder = Cylinder(self.x, self.y, 0, self.outerRadius * 2 - 2*self.thickness - self.toothradius, self.depth)

        mainCylinder.subtract(subtractCylinder)

        mainBlock = Block(xBlock, self.y, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height)

        subtractBlock = Block(xBlock, self.y + self.thickness, mainCylinder.z + self.thickness,
                               4*self.outerRadius, self.gearRadius - self.thickness, mainCylinder.height - 2*self.thickness)

        mainBlock.subtract(subtractBlock)

        subtractCylinder = Cylinder(self.x, self.y, 0, self.outerRadius * 2 - 2*self.thickness - self.toothradius, self.depth)
        
        mainBlock.subtract(subtractCylinder)

        mainCylinder.unite(mainBlock)

        subtractBlock = Block(xBlock, self.y + self.thickness, mainCylinder.z + self.thickness,
                               4*self.outerRadius, self.gearRadius*2, mainCylinder.height - 2*self.thickness)

        mainCylinder.subtract(subtractBlock)

        subtractBlock2 = Block(xBlock, self.y + self.gearRadius, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height)

        mainCylinder.subtract(subtractBlock2)