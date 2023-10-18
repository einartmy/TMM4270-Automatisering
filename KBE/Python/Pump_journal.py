# from Shapes.Pump_Gears import Pump_Gears
# from Case_parts import UpperCase, LowerCase
# from Motion.Motion3 import Motion3
# import random
from Calculate_pump import CalculatePump
import json
import os

class Pump:

    def __init__(self, targetVpm, case_thickness = 30, x = 0, y = 0):
        self.targetVpm = targetVpm
        self.case_thickness = case_thickness
        self.x = x
        self.y = y
        self.radius = 0
        self.teeth_radius = 0
        self.depth = 0

        self.createPump()


    def createPump(self):
        calculatePump = CalculatePump()                 
        calculatePump.change_pump(self.targetVpm)           #Converting pump to wished size
        self.radius = calculatePump.radius * 1000                #Convert to mm
        self.depth = calculatePump.depth * 1000                  #Convert to mm
        self.teeth_radius = calculatePump.teeth_radius * 1000     #Convert to mm
        print(f'radius funnet ved vpm: {self.targetVpm} m^3 pr. min, ble verdien av radiusen {round(self.radius/1000,4)} m')

        # gear1 = Pump_Gears(radius, depth, teethradius, self.x, self.y, False)                     #making 1st gear
        # gear2 = Pump_Gears(radius, depth, teethradius, self.x, self.y - 2*radius, True)           #making 2nd gear

        # case1 = UpperCase(radius, depth, teethradius, self.case_thickness, self.x, self.y)             
        # case2 = LowerCase(radius, depth, teethradius, self.case_thickness, self.x, self.y - 2*radius)

    def get_design_parameters(self):
        return {
            "targetVpm": self.targetVpm,
            "case_thickness": self.case_thickness,
            "x": self.x,
            "y": self.y,
            "calculated_radius": round(self.radius, 5),
            "calculated_depth": round(self.depth, 5),
            "calculated_teethradius": round(self.teeth_radius, 5),
            # ... [any other parameters you want to save] ...
        }

if __name__ == "__main__":
    with open("KBE/Python/Pump_parameters.json", "r") as file:
        params = json.load(file)
    
    # Use the loaded parameters to create a Pump instance
    pump = Pump(**params)

    # Gather design parameters
    design_params = pump.get_design_parameters()

    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(current_directory, "Design_parameters_output.json")

    # Save the design parameters to a JSON output file
    with open(output_file_path, "w") as file:
        json.dump(design_params, file, indent=4)

    # targetVpm = 5  # Adjust this value as needed
    # Pump(targetVpm)



