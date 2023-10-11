from Shapes.Pump_Gears import Pump_Gears
from Case_parts import upperCase

radius = 100
depth = 50
teethradius = 20
x = 10
y = 200
caseThickness = 10

gear1 = Pump_Gears(radius, depth, teethradius, x, y, False)
gear2 = Pump_Gears(radius, depth, teethradius, x, y - 2*radius, True)

case1 = upperCase(radius, depth, teethradius, caseThickness, x, y)

from Case import UpperCase, LowerCase, Wall

# upper_case = UpperCase(gear1.x, gear1.y, gear1.gearRadius + 0.5*gear1.teethRadius, gear1.gearHeight)
# lower_case = LowerCase(gear2.x, gear2.y, gear2.gearRadius + gear2.teethRadius, gear2.gearHeight)
# wall = Wall(gear1.x, gear1.y, gear1.gearRadius, gear1.gearHeight, 10, gear1.teethRadius)