from Shapes.Cylinder import Cylinder
import NXOpen
import math


class Pump_Gears:
	
    def __init__(self, gearRadius, gearHeight, teethRadius, x, y, offset):
        self.gearRadius = gearRadius
        self.gearHeight = gearHeight
        self.x = x
        self.y = y
        self.teethRadius = teethRadius
        self.offset = offset
        self.gear = Cylinder(self.x, self.y, 0, self.gearRadius*2, self.gearHeight)
        
        
        #self.gearRadius = 0.5 * circumference* (1/math.pi)

        self.initForNX()


    def initForNX(self):
        
        circumference = 2*self.gearRadius * math.pi
        numberOfTeeth = math.ceil(circumference * 0.5 * (1/self.teethRadius))

        radius = self.gearRadius
        # circumference = self.numberOfTeeth * 2 * self.teethRadius
        # radius = 0.5 * circumference* (1/math.pi)
        gear = self.gear

        numberOfTeeth = numberOfTeeth * 2
        

        angle = 2* math.pi / numberOfTeeth

        for i in range(0, numberOfTeeth):
            if self.offset: 
                tooth = Cylinder(self.x + (radius*math.cos(i*angle + angle)), self.y + (radius*math.sin(i*angle + angle)), 0, self.teethRadius, self.gearHeight)
            else:
                tooth = Cylinder(self.x + (radius*math.cos(i*angle)), self.y + (radius*math.sin(i*angle)), 0, self.teethRadius, self.gearHeight)

            if i % 2 == 0:
                gear.subtract(tooth)
            
            else:
                gear.unite(tooth)


        hole_in_gear = Cylinder(self.x, self.y, 0, radius/15, self.gearHeight, [0,0,1])
        gear.subtract(hole_in_gear)
            
        
        