import math

class CalculatePump:
    def __init__(self, radius = 0.001, teethDiameterRatio=5, angleSpeed=1):              #A standard gearupset that seems reasonably related to each other, possible to change,
        self.radius = radius                                                              #Radius starts with a low value for the calculations
        self.teethDiameterRatio = teethDiameterRatio
        self.teethDiameter = radius / teethDiameterRatio
        self.angleSpeed = angleSpeed
        self.depth = 2 * radius

    def numberOfTeeth(self):                                                          #A function to calculate amount of gear teeths
        return math.ceil(2 * self.radius * math.pi * 0.5 * (1 / self.teethDiameter))

    def vpm(self):  
        teeths = self.numberOfTeeth()
        angle = 2 * math.pi / teeths                                                    #Finding the angels between the teeth
        korde = ((self.radius + self.teethDiameter)**2 * (angle - math.sin(angle))) / 2  #Finding the area of the korde using angle
        areal = 4 * (self.teethDiameter** 2) + korde                                     #Finding the area between 2 teeth
        volume = areal * self.depth                                                     #Finding the volume of 1 teeth

        rpm = self.angleSpeed * 60 / (2 * math.pi * self.radius)                       #Calculating how many times the wheel spin around in a min
        return volume * teeths * rpm * 2                                                #Multiply volume pr teeth and theeths and how ofte a teeth comes around (*2 because 2 gears)

    def changePump(self, targetVpm):
        while targetVpm >= self.vpm():                             #While loop that checks different sizes until you get a radius and matching gear that produce wanted volume pr. min
            self.radius += 0.005        
            self.depth = 2 * self.radius
            self.teethDiameter = self.radius / self.teethDiameterRatio
        





# Example usage:
if __name__ == "__main__":
    targetVpm = 1000  # Adjust this value as needed
    pump = CalculatePump()
    pump.changePump(targetVpm)
    print(f"Final radius to achieve {targetVpm} VPM: {round(pump.radius, 4)}")
