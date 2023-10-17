#from Shapes.Pump_Gears import Pump_Gears
#from Case_parts import UpperCase, LowerCase
#from Motion.Motion3 import Motion3
import random
from Calculate_pump import CalculatePump

class Pump:
    
    def __init__(self, targetVpm, caseThickness = 30, x = 0, y = 0):
        self.TargetVpm = targetVpm
        self.caseThickness = caseThickness
        self.x = x
        self.y = y
        
        self.createPump()
    
    
    def createPump(self):
        calculatePump = CalculatePump()
        calculatePump.change_pump(targetVpm)
        radius = calculatePump.radius * 1000  #Convert to mm

        depth = 2*radius
        teethradius = calculatePump.teeth_radius
        print(f'radius funnet ved vpm: {targetVpm} Liter pr. min, ble verdien av radiusen {radius/1000} m')
        # gear1 = Pump_Gears(radius, depth, teethradius, self.x, self.y, False)
        # gear2 = Pump_Gears(radius, depth, teethradius, self.x, self.y - 2*radius, True)

        # case1 = UpperCase(radius, depth, teethradius, self.caseThickness, self.x, self.y)
        # case2 = LowerCase(radius, depth, teethradius, self.caseThickness, self.x, self.y - 2*radius)


if __name__ == "__main__":
    targetVpm = 1000  # Adjust this value as needed
    Pump(targetVpm)
    
    
    #print(f"Final radius to achieve {target_vpm} VPM: {pump.radius}")
# pathToTheFolder = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Animation\\"
# fileName = "geartrain_" + str(random.randint(1,10000)) 

# motion = Motion3([gear1.gear, gear2.gear], 0, 10, 10, 0, True, pathToTheFolder, fileName)

