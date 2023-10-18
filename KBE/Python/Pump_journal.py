# from Shapes.Pump_Gears import Pump_Gears
# from Case_parts import UpperCase, LowerCase
# from Motion.Motion3 import Motion3
# import random
from datetime import datetime
from Calculate_pump import CalculatePump
import json
import os
import pandas as pd

class Pump:

    def __init__(self, targetVpm, case_thickness = 30, x = 0, y = 0):
        self.targetVpm = targetVpm
        self.case_thickness = case_thickness
        self.x = x
        self.y = y
        self.radius = 0
        self.teeth_radius = 0
        self.depth = 0
        self.angle_speed = 0

        self.createPump()


    def createPump(self):
        calculatePump = CalculatePump()                 
        calculatePump.change_pump(self.targetVpm)           #Converting pump to wished size
        self.radius = calculatePump.radius * 1000                #Convert to mm
        self.depth = calculatePump.depth * 1000                  #Convert to mm
        self.teeth_radius = calculatePump.teeth_radius * 1000    #Convert to mm
        self.angle_speed = calculatePump.angle_speed
        print(f'radius funnet ved vpm: {self.targetVpm} m^3 pr. min, ble verdien av radiusen {round(self.radius/1000,4)} m')

        # gear1 = Pump_Gears(radius, depth, teethradius, self.x, self.y, False)                     #making 1st gear
        # gear2 = Pump_Gears(radius, depth, teethradius, self.x, self.y - 2*radius, True)           #making 2nd gear

        # case1 = UpperCase(radius, depth, teethradius, self.case_thickness, self.x, self.y)             
        # case2 = LowerCase(radius, depth, teethradius, self.case_thickness, self.x, self.y - 2*radius)

    def get_design_parameters(self):
        data = {
            "metadata": {
            "timestamp": str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S")),
            "description": "Design parameters for the pump.",
            },
            "volumePerMinuteTarget": {
                "value": self.targetVpm,
                "unit": "cubic meters per minute",
                "comment": "Desired volume throughput of the pump"
            },
            "parameters": {
                "unit": "millimeters",
                "calculated radius": round(self.radius, 5),
                "calculated depth": round(self.depth, 5),
                "calculated teethradius": round(self.teeth_radius, 5),
                "casing thickness": self.case_thickness,
                "x position (center of upper gear)": self.x,
                "y position (center of upper gear)": self.y,
                "angle speed": self.angle_speed,
            }
            }
        
        return data

if __name__ == "__main__":
    with open("KBE/Python/Pump_parameters.json", "r") as file:
        params = json.load(file)
    
    # Use the loaded parameters to create a Pump instance
    pump = Pump(**params)

    # Gather design parameters
    design_params = pump.get_design_parameters()

    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_json_path = os.path.join(current_directory, "Design_parameters_output.json")

    # Save the design parameters to a constant JSON output file
    with open(output_json_path, "w") as file:
        json.dump(design_params, file, indent=4)

    #Save the design parameters to a new txt file each time a pump design is made
    current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    
    # Name of the directory where you want to save your txt files
    directory_name = "txt_output_files"
    output_folder_path = os.path.join(current_directory, directory_name)

    # Check if the directory exists. If not, create it.
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # Create unique filename with the timestamp and directory
    filename = os.path.join(output_folder_path, f"Desing_paramaters_output_{current_time}.txt")
    
    # Save the data in the txt file
    with open(filename, 'w') as outfile:
        json.dump(design_params, outfile, indent=4)
            




