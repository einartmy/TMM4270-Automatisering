import math

class CalculatePump:
    def __init__(self, radius = 0.1, teeth_radius_ratio=5, angle_speed=1):
        self.radius = radius
        self.teeth_radius_ratio = teeth_radius_ratio
        self.teeth_radius = radius / teeth_radius_ratio
        self.angle_speed = angle_speed
        self.depth = 2 * radius

    def number_of_teeth(self): #A function to calculate amount of gear teeths
        return math.ceil(2 * self.radius * math.pi * 0.5 * (1 / self.teeth_radius))

    def vpm(self):
        self.depth = 2 * self.radius
        self.teeth_radius = self.radius / self.teeth_radius_ratio
        teeths = self.number_of_teeth()

        angle = 2 * math.pi / teeths
        korde = ((self.radius + self.teeth_radius) ** 2 * math.sin(angle)) / 2
        areal = 4 * self.teeth_radius ** 2 + korde
        volume = areal * self.depth

        rpm = self.angle_speed * 60 / (2 * math.pi * self.radius)  # Use instance variable
        return volume * teeths * rpm * 2

    def change_pump(self, target_vpm):
        while target_vpm > self.vpm():
            self.radius += 0.1
        

# Example usage:
if __name__ == "__main__":
    initial_radius = 0.1
    target_vpm = 1000  # Adjust this value as needed
    pump = CalculatePump(initial_radius)
    pump.change_pump(target_vpm)
    print(f"Final radius to achieve {target_vpm} VPM: {pump.radius}")
