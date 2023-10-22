import math
from Shapes.Cylinder import Cylinder
from Shapes.Block import Block

class UpperCase:

    def __init__(self, gearRadius, gearDepth, toothradius, thickness, x, y):
        self.gearRadius = gearRadius
        self.toothradius = toothradius
        self.outerRadius = gearRadius + toothradius + thickness         #Radius from center to outside the casing
        self.depth = gearDepth                                          #Depth inside the case, same as gear depth
        self.thickness = thickness                                      
        self.x = x
        self.y = y
        self.initForNX()

    def initForNX(self):
        xBlock = self.x - 2* self.outerRadius
        yBlock = self.y - self.gearRadius


        mainCylinder = Cylinder(self.x, self.y, -self.thickness, self.outerRadius * 2 - self.toothradius, self.depth + 2*self.thickness) #Create cylinderCase
        mainBlock = Block(xBlock, yBlock, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height ) #Create blockCase
        mainCylinder.unite(mainBlock)


        subtractCylinder = Cylinder(self.x, self.y, 0, (2*self.outerRadius) - (2*self.thickness) - self.toothradius, self.depth)
        mainCylinder.subtract(subtractCylinder) #Create CaseSubract to fit the gear

        subtractBlock = Block(xBlock, yBlock,   mainCylinder.z + self.thickness,  4*self.outerRadius, self.gearRadius - self.thickness,   mainCylinder.height - 2*self.thickness) 
        mainCylinder.subtract(subtractBlock) #Create CaseSubract to fit the in and out tube

        subtractBlock2 = Block(xBlock, yBlock - self.gearRadius, mainCylinder.z,  4*self.outerRadius, self.gearRadius,  mainCylinder.height)
        mainCylinder.subtract(subtractBlock2) #Create CaseSubract to remove the cylinder that overlaps with lowerCase
 

    def getVolume(self):
        # Calculation based on cylinder volume formula
        outer_cyl_volume = math.pi * (self.outerRadius**2) * self.depth
        inner_cyl_volume = math.pi * (self.outerRadius - self.thickness)**2 * (self.depth - 2*self.thickness)
        #Calculatios on suction and dischage volume
        outer_block_volume = self.gearRadius**2 *self.depth*2
        inner_block_volume = self.gearRadius * (self.gearRadius - self.thickness)*(self.depth - 2*self.thickness) *2
        return (outer_cyl_volume - inner_cyl_volume) * 1/2 + (outer_block_volume - inner_block_volume)



class LowerCase:

    def __init__(self, gearRadius, gearDepth, toothradius, thickness, x, y):
        self.gearRadius = gearRadius
        self.toothradius = toothradius
        self.outerRadius = gearRadius + toothradius + thickness         #Radius from center to outside the casing
        self.depth = gearDepth                                          #Depth inside the case, same as gear depth
        self.thickness = thickness                                      
        self.x = x
        self.y = y
        

        self.initForNX()

    def initForNX(self):
        xBlock = self.x - 2* self.outerRadius

        mainCylinder = Cylinder(self.x, self.y, -self.thickness, self.outerRadius * 2 - self.toothradius, self.depth + 2*self.thickness)
        mainBlock = Block(xBlock, self.y, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height)
        mainCylinder.unite(mainBlock)
        
        subtractCylinder = Cylinder(self.x, self.y, 0, self.outerRadius * 2 - 2*self.thickness - self.toothradius, self.depth)
        mainCylinder.subtract(subtractCylinder)
        
        subtractBlock = Block(xBlock, self.y + self.thickness, mainCylinder.z + self.thickness,4*self.outerRadius, self.gearRadius - self.thickness, mainCylinder.height - 2*self.thickness)
        mainCylinder.subtract(subtractBlock)

        subtractBlock2 = Block(xBlock, self.y + self.gearRadius, mainCylinder.z , 4*self.outerRadius, self.gearRadius, mainCylinder.height)
        mainCylinder.subtract(subtractBlock2)

        

    def getVolume(self):
        # Calculation based on cylinder volume formula
        outer_cyl_volume = math.pi * (self.outerRadius**2) * self.depth
        inner_cyl_volume = math.pi * (self.outerRadius - self.thickness)**2 * (self.depth - 2*self.thickness)
        #Calculatios on suction and dischage volume
        outer_block_volume = self.gearRadius**2 *self.depth*2
        inner_block_volume = self.gearRadius * (self.gearRadius - self.thickness)*(self.depth - 2*self.thickness) *2
        return (outer_cyl_volume - inner_cyl_volume) * 1/2 + (outer_block_volume - inner_block_volume)