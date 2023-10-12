from Shapes.Pump_Gears import Pump_Gears
from Case_parts import upperCase, lowerCase
from Motion.Motion3 import Motion3
import random

radius = 100
depth = radius
teethradius = radius/5
x = 0
y = 0
caseThickness = 15

gear1 = Pump_Gears(radius, depth, teethradius, x, y, False)
gear2 = Pump_Gears(radius, depth, teethradius, x, y - 2*radius, True)

case1 = upperCase(radius, depth, teethradius, caseThickness, x, y)
case2 = lowerCase(radius, depth, teethradius, caseThickness, x, y - 2*radius)

pathToTheFolder = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Animation\\"
fileName = "geartrain_" + str(random.randint(1,10000)) 

motion = Motion3([gear1.gear, gear2.gear], 0, 10, 10, 0, True, pathToTheFolder, fileName)