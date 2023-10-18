# from Shapes.Pump_Gears import Pump_Gears
# from Case_parts import UpperCase, LowerCase
# from Motion.Motion3 import Motion3
# import random
from Calculate_pump import CalculatePump
import json

class Pump:

    def __init__(self, targetVpm, caseThickness = 30, x = 0, y = 0):
        self.targetVpm = targetVpm
        self.caseThickness = caseThickness
        self.x = x
        self.y = y

        self.createPump()


    def createPump(self):
        calculatePump = CalculatePump()                 
        calculatePump.change_pump(self.targetVpm)           #Converting pump to wished size
        radius = calculatePump.radius * 1000                #Convert to mm
        depth = calculatePump.depth * 1000                  #Convert to mm
        teethradius = calculatePump.teeth_radius * 1000     #Convert to mm
        print(f'radius funnet ved vpm: {self.targetVpm} m^3 pr. min, ble verdien av radiusen {round(radius/1000,4)} m')

        # gear1 = Pump_Gears(radius, depth, teethradius, self.x, self.y, False)                     #making 1st gear
        # gear2 = Pump_Gears(radius, depth, teethradius, self.x, self.y - 2*radius, True)           #making 2nd gear

        # case1 = UpperCase(radius, depth, teethradius, self.caseThickness, self.x, self.y)             
        # ase2 = LowerCase(radius, depth, teethradius, self.caseThickness, self.x, self.y - 2*radius)


if __name__ == "__main__":
    with open("KBE/Python/Pump_parameters.json", "r") as file:
        params = json.load(file)
    
    pump = Pump(**params)

    # targetVpm = 5  # Adjust this value as needed
    # Pump(targetVpm)



