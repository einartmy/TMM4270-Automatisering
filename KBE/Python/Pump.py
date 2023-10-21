from Pump_parts.Pump_Gears import Pump_Gears
from Pump_parts.Case_parts import UpperCase, LowerCase
from Motion.Motion3 import Motion3
import random
from datetime import datetime
import math
from Calculate_pump import CalculatePump
import json
import os

class Pump:

    def __init__(self, targetVpm, caseThickness = 30, x = 0, y = 0):
        self.targetVpm = targetVpm
        self.caseThickness = caseThickness
        self.x = x
        self.y = y
        self.radius = 0
        self.teethDiameter = 0
        self.depth = 0
        self.angleSpeed = 0
        self.density = 2700                     #Aluminium density
        self.mass = 0

        self.createPump()


    def createPump(self):
        calculatePump = CalculatePump()                 
        calculatePump.changePump(self.targetVpm)           #Converting pump to wished size
        self.radius = calculatePump.radius * 1000                #Convert to mm
        self.depth = calculatePump.depth * 1000                  #Convert to mm
        self.teethDiameter = calculatePump.teethDiameter * 1000    #Convert to mm
        self.angleSpeed = calculatePump.angleSpeed
        print(f'radius funnet ved vpm: {self.targetVpm} m^3 pr. min, ble verdien av radiusen {round(self.radius/1000,4)} m')

        self.gear1 = Pump_Gears(self.radius, self.depth, self.teethDiameter, self.x, self.y, False)                    
        self.gear2 = Pump_Gears(self.radius, self.depth, self.teethDiameter, self.x, self.y - 2*self.radius, True)

        upperCase = UpperCase(self.radius, self.depth, self.teethDiameter, self.caseThickness, self.x, self.y)
        lowerCase = LowerCase(self.radius, self.depth, self.teethDiameter, self.caseThickness, self.x, self.y - 2*self.radius)

        volume = self.calculateVolume(self.gear1, self.gear2, upperCase, lowerCase)       #Calculating volume
        self.mass = self.density * volume                                                   #Calculating mass


    def getDesignParameters(self):
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
                "calculated teethDiameter": round(self.teethDiameter, 5),
                "casing thickness": self.caseThickness,
                "x position (center of upper gear)": self.x,
                "y position (center of upper gear)": self.y,
                "angle speed": self.angleSpeed,
                
                "mass unit": "kg",
                "pump mass": self.mass,

                "pump material": "Aluminium",
                "pump density": self.density,
                "density unit": "kg pr cubic meter"
            }
            }
        
        return data

    def calculateVolume(self, gear1, gear2, upperCase, lowerCase):
        # Calculating volume of the two gears 
        volumeGear1 = gear1.calculateVolume()
        volumeGear2 = gear2.calculateVolume()  # since they are of the same dimensions

        # Calculating volume of the casing (upper and lower)
        volumeUpperCase = upperCase.getVolume()
        volumeLowerCase = lowerCase.getVolume()

        # Summing up the volume of the casing and the gears
        totalVolume = volumeUpperCase + volumeLowerCase + volumeGear1 + volumeGear2
        
        #Converting to cubic meters from cubic millimeters and returning volume
        return totalVolume * 10e-9    


if __name__ == "__main__":
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    inputJsonPath = os.path.join(currentDirectory, "Pump_parameters.json")
    with open(inputJsonPath, "r") as file:
        params = json.load(file)
    
    # Use the loaded parameters to create a Pump instance
    pump = Pump(**params)

    # Gather design parameters
    designParams = pump.getDesignParameters()

    outputJsonPath = os.path.join(currentDirectory, "Design_parameters_output.json")

    # Save the design parameters to a constant JSON output file
    with open(outputJsonPath, "w") as file:
        json.dump(designParams, file, indent=4)

    #Save the design parameters to a new txt file each time a pump design is made
    currentTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Name of the directory where you want to save your txt files
    directory_name = "txt_output_files"
    outputFolderPath = os.path.join(currentDirectory, directory_name)

    # Check if the directory exists. If not, create it.
    if not os.path.exists(outputFolderPath):
        os.makedirs(outputFolderPath)
    
    # Create unique filename with the timestamp and directory
    filename = os.path.join(outputFolderPath, f"Desing_paramaters_output_{currentTime}.txt")
    
    # Save the data in the txt file
    with open(filename, 'w') as outfile:
        json.dump(designParams, outfile, indent=4)
    
    # pathToTheFolder = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Animation\\"
    # fileName = "geartrain_" + str(random.randint(1,10000)) 

    # cyl1 = pump.gear1.gear
    # cyl2 = pump.gear2.gear


    # motion = Motion3([cyl1, cyl2], 0, 10, 10, 0, True, pathToTheFolder, fileName)
            




