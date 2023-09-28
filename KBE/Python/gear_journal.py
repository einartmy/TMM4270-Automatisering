from Shapes.Gear import Gear

gear1 = Gear(100, 15, 40, 0, 0)
gear2 = Gear(gear1.gearR, gear1.toothL, gear1.gearHeight, gear1.x, -2*gear1.gearR + gear1.toothL*0.8)