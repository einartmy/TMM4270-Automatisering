import math

class CalculatePump:
    def __init__(self, radius = 0.001, teeth_radius_ratio=5, angle_speed=1):              #A standard gearupset that seems reasonably related to each other, possible to change,
        self.radius = radius                                                              #Radius starts with a low value for the calculations
        self.teeth_radius_ratio = teeth_radius_ratio
        self.teeth_radius = radius / teeth_radius_ratio
        self.angle_speed = angle_speed
        self.depth = 2 * radius

    def number_of_teeth(self):                                                          #A function to calculate amount of gear teeths
        return math.ceil(2 * self.radius * math.pi * 0.5 * (1 / self.teeth_radius))

    def vpm(self):  
        teeths = self.number_of_teeth()
        angle = 2 * math.pi / teeths                                                    #Finding the angels between the teeth
        korde = ((self.radius + self.teeth_radius)**2 * (angle - math.sin(angle))) / 2  #Finding the area of the korde using angle
        areal = 4 * (self.teeth_radius** 2) + korde                                     #Finding the area between 2 teeth
        volume = areal * self.depth                                                     #Finding the volume of 1 teeth

        rpm = self.angle_speed * 60 / (2 * math.pi * self.radius)                       #Calculating how many times the wheel spin around in a min
        return volume * teeths * rpm * 2                                                #Multiply volume pr teeth and theeths and how ofte a teeth comes around (*2 because 2 gears)

    def change_pump(self, target_vpm):
        while target_vpm > self.vpm():                             #While loop that checks different sizes until you get a radius and matching gear that produce wanted volume pr. min
            self.radius += 0.005        
            self.depth = 2 * self.radius
            self.teeth_radius = self.radius / self.teeth_radius_ratio
        





# Example usage:
if __name__ == "__main__":
    target_vpm = 1000  # Adjust this value as needed
    pump = CalculatePump()
    pump.change_pump(target_vpm)
    print(f"Final radius to achieve {target_vpm} VPM: {round(pump.radius, 4)}")
