from Shapes.Pump_Gears import Pump_Gears

gear1 = Pump_Gears(100, 10, 33, 50, 50)
gear2 = Pump_Gears(gear1.gearRadius, gear1.gearHeight, gear1.teethRadius, gear1.x - 2*gear1.gearRadius, gear1.y)

from Case import UpperCase, LowerCase, Wall

# upper_case = UpperCase(gear1.x, gear1.y, gear1.gearRadius, gear1.gearHeight)
# lower_case = LowerCase(gear2.x, gear2.y, gear2.gearRadius, gear2.gearHeight)
# wall = Wall(gear1.x, gear1.y, gear1.gearRadius, gear1.gearHeight, 10, gear1.teethRadius)