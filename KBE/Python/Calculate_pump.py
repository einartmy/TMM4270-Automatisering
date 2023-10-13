import math

class CalculatePump:
    def __init__(self, radius, teeth_radius_ratio=5, angle_speed=1):
        self.radius = radius
        self.gear_radius = radius
        self.teeth_radius = radius / teeth_radius_ratio
        self.angle_speed = angle_speed

    def number_of_teeth(self): #A function to calculate amount of gear teeths
        return math.ceil(2 * self.gear_radius * math.pi * 0.5 * (1 / self.teeth_radius))

    def vpm(self):
        depth = 2 * self.radius
        teethradius = self.teeth_radius  # Use instance variable
        angleSpeed = self.angle_speed  # Use instance variable
        teeths = self.number_of_teeth()

        angle = 2 * math.pi / teeths
        korde = ((self.radius + teethradius) ** 2 * math.sin(angle)) / 2
        areal = 4 * teethradius ** 2 + korde
        volume = areal * depth

        rpm = angleSpeed * 60 / (2 * math.pi * self.radius)  # Use instance variable
        return volume * teeths * rpm * 2

    def get_pump(self, target_vpm):
        while target_vpm > self.vpm():
            self.radius += 0.02

# Example usage:
if __name__ == "__main__":
    initial_radius = 0.1
    target_vpm = 1000  # Adjust this value as needed
    pump = CalculatePump(initial_radius)
    pump.get_pump(target_vpm)
    print(f"Final radius to achieve {target_vpm} VPM: {pump.radius}")
