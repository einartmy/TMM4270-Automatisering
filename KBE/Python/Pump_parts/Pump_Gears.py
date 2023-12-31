from Shapes.Cylinder import Cylinder
import math


class Pump_Gears:
	
    def __init__(self, gearRadius, gearHeight, teethDiameter, x, y, offset):
        self.gearRadius = gearRadius                                            #Radius of gears main cylinder
        self.gearHeight = gearHeight                                            #Height also known as debth of the gear
        self.x = x
        self.y = y                                                                  
        self.teethDiameter = teethDiameter                                         #The diameter of a single tooth
        self.offset = offset                                                        #Offset to know what type of gear we are building, slave or master (upper or lower), for meshing purposes.
        self.gear = Cylinder(self.x, self.y, 0, self.gearRadius*2, self.gearHeight) #Main gear using a Cylinder as its base
        
    
        self.initForNX()


    def initForNX(self):
        
        circumference = 2*self.gearRadius * math.pi                             #Calculating circumference
        numberOfTeeth = math.ceil(circumference * 0.5 * (1/(self.teethDiameter)))   #Finding suitable amount of gear teeth

        radius = self.gearRadius                                                #To save time

        numberOfTeeth = numberOfTeeth * 2                                       #Duplicate teeth so the gear has indents as well
        angle = 2* math.pi / numberOfTeeth                                      #Finding the offset angle for a single teeth

        for i in range(0, numberOfTeeth):                                       #Running threw all the teeths
            if self.offset:                                                     #Offset so the 2 gears wont collide
                tooth = Cylinder(self.x + (radius*math.cos(i*angle + angle)), self.y + (radius*math.sin(i*angle + angle)), 0, self.teethDiameter, self.gearHeight)             
            else:
                tooth = Cylinder(self.x + (radius*math.cos(i*angle)), self.y + (radius*math.sin(i*angle)), 0, self.teethDiameter, self.gearHeight)

            if i % 2 == 0:                                                      #Subtract 1 and then unite 1                                          
                self.gear.subtract(tooth)
            else:
                self.gear.unite(tooth)


        holeIngear = Cylinder(self.x, self.y, 0, radius/15, self.gearHeight, [0,0,1])   #Creating hole in gear
        self.gear.subtract(holeIngear)

    def calculateVolume(self):
        # Main Gear Volume
        volumegear = math.pi * (self.gearRadius**2) * self.gearHeight

        # Hole in the Gear Volume
        holeRadius = self.gearRadius / 15
        volumeHole = math.pi * (holeRadius**2) * self.gearHeight

        # Total volume of the gear considering the hole
        total_volume = volumegear - volumeHole
        
        return total_volume
            
        
        