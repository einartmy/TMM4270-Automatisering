from Shapes.Gear import Gear
from Case import UpperCase, LowerCase, Wall
import random
from Motion.Motion3 import Motion3

gear1 = Gear(100, 40, 20, 40, 50, 100)
gear2 = Gear(gear1.gearR, gear1.toothLength, gear1.toothWidth, gear1.gearHeight, gear1.x, gear1.y-2*gear1.gearR - 0.5*gear1.toothLength)


upper_case = UpperCase(gear1.x, gear1.y, gear1.gearR + gear1.toothLength*0.5 , gear1.gearHeight)
lower_case = LowerCase(gear2.x, gear2.y, gear2.gearR + gear2.toothLength*0.5, gear2.gearHeight)
wall = Wall(gear1.x, gear1.y, upper_case.gear_radius, gear1.gearHeight, 10, gear1.toothLength)

pathToTheFolder = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Animation\\"
fileName = "geartrain_" + str(random.randint(1,10000)) 

#motion = Motion3([gear1, gear2], 0, 10, 10, 0, True, pathToTheFolder, fileName)