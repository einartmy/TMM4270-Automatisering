from Shapes.Gear import Gear

gear1 = Gear(70, 10, 10, 20, 0, 0)
gear2 = Gear(gear1.gearR, gear1.toothLength, gear1.toothWidth, gear1.gearHeight, gear1.x, -2*gear1.gearR + gear1.toothLength*0.7)