from Shapes.Gear import Gear
from case import Case

gear1 = Gear(170, 10, 10, 40, 50, 100)
gear2 = Gear(gear1.gearR, gear1.toothLength, gear1.toothWidth, gear1.gearHeight, gear1.x, gear1.y-2*gear1.gearR + gear1.toothLength*0.7)


upper_case = Case(gear1.x, gear1.y, gear1.gearR, gear1.gearHeight)