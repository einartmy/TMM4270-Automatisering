from Shapes.Gear import Gear
from Case import UpperCase, LowerCase

gear1 = Gear(100, 20, 20, 40, 50, 100)
gear2 = Gear(gear1.gearR, gear1.toothLength, gear1.toothWidth, gear1.gearHeight, gear1.x, gear1.y-2*gear1.gearR + gear1.toothLength*0.7)


upper_case = UpperCase(gear1.x, gear1.y, gear1.gearR, gear1.gearHeight)
lower_case = LowerCase(gear2.x, gear2.y, gear2.gearR, gear2.gearHeight)