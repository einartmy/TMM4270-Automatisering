# from Shapes.Pump_Gears import Pump_Gears
# from Case_parts import UpperCase, LowerCase
# from Motion.Motion3 import Motion3
# import random
from datetime import datetime
import math
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
        self.density = 2700 #Aluminium density
        self.mass = 0

        self.createPump()


    def createPump(self):
        calculatePump = CalculatePump()                 
        calculatePump.change_pump(self.targetVpm)           #Converting pump to wished size
        self.radius = calculatePump.radius * 1000                #Convert to mm
        self.depth = calculatePump.depth * 1000                  #Convert to mm
        self.teeth_radius = calculatePump.teeth_radius * 1000    #Convert to mm
        self.angle_speed = calculatePump.angle_speed
        print(f'radius funnet ved vpm: {self.targetVpm} m^3 pr. min, ble verdien av radiusen {round(self.radius/1000,4)} m')

        # gear1 = Pump_Gears(self.radius, self.depth, self.teeth_radius, self.x, self.y, False)                    
        # gear2 = Pump_Gears(self.radius, self.depth, self.teeth_radius, self.x, self.y - 2*self.radius, True)

        # upper_case = UpperCase(self.radius, self.depth, self.teeth_radius, self.case_thickness, self.x, self.y)
        # lower_case = LowerCase(self.radius, self.depth, self.teeth_radius, self.case_thickness, self.x, self.y - 2*self.radius)

        # volume = self.calculate_volume(gear1, gear2, upper_case, lower_case)       #Calculating volume
        # self.mass = self.density * volume                                          #Calculating mass


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
                "length unit": "millimeters",
                "calculated radius": round(self.radius, 5),
                "calculated depth": round(self.depth, 5),
                "calculated teethradius": round(self.teeth_radius, 5),
                "casing thickness": self.case_thickness,
                "x position (center of upper gear)": self.x,
                "y position (center of upper gear)": self.y,
                "angle speed": self.angle_speed,
                
                "mass unit": "kg",
                "pump mass": self.mass,

                "pump material": "Aluminium",
                "pump density": self.density,
                "density unit": "kg pr cubic meter"
            }
            }
        
        return data

    def calculate_volume(self, gear1, gear2, upper_case, lower_case):
        # Calculating volume of the two gears 
        volume_gear1 = gear1.calculate_volume()
        volume_gear2 = volume_gear1  # since they are of the same dimensions

        # Calculating volume of the casing (upper and lower)
        volume_upper_case = upper_case.get_volume()
        volume_lower_case = lower_case.get_volume()

        # Summing up the volume of the casing and the gears
        total_volume = volume_upper_case + volume_lower_case + volume_gear1 + volume_gear2
        
        #Converting to cubic meters from cubic millimeters and returning volume
        return total_volume * 10e-9    


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
            




