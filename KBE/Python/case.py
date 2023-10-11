import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\TMM4270-Automatisering\KBE\Python")
##

from Shapes.Swept import Swept 
from Shapes.Line import Line 
from Shapes.Arc import Arc
from Shapes.Cylinder import Cylinder

class UpperCase:

    def __init__(self, gear_center_x, gear_center_y, gear_radius, depth):
        self.depth = depth
        self.gear_center_x = gear_center_x
        self.gear_center_y = gear_center_y
        self.gear_radius = gear_radius

        def create_line(x_start, y_start, x_end, y_end, depth_start, depth_end):
            return Line(x_start, y_start, depth_start, x_end, y_end, depth_end)
        
        def create_swept(main_line, base_lines):
            return Swept([main_line], base_lines)
        
        half_gear_radius = gear_radius * 0.5
        y_position = gear_center_y - half_gear_radius

        # Create first swept object
        
        #Creating guide
        line1 = create_line(gear_center_x - gear_radius - 10, y_position, gear_center_x - gear_radius - 10, gear_center_y, 0, 0)
        arc_g1 = Arc(gear_center_x, gear_center_y, 0, (1, 0, 0), (0, 1, 0), gear_radius + 10, 0, 180)
        line2 = create_line(gear_center_x + gear_radius + 10, y_position, gear_center_x + gear_radius + 10, gear_center_y, 0, 0)
        
        #Creating section
        base_lines = [
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 5, y_position, depth, depth),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 15, y_position, 0, 0),
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 15, y_position, 0, depth)
        ]
        swept = Swept([line1, arc_g1, line2], base_lines)

        # Create second swept object
        
        #Guide
        line3 = create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 110, y_position, 0, 0)
        
        #Section
        base_lines = [
            create_line(gear_center_x - gear_radius - 5, y_position + 10, gear_center_x - gear_radius - 5, y_position + 10, 0, depth),
            create_line(gear_center_x - gear_radius - 5, y_position + 10, gear_center_x - gear_radius - 5, y_position, depth, depth),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position + 10, 0, 0)
        ]
        swept2 = create_swept(line3, base_lines)


        # Create third swept object

        #Guide
        line4 = create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 110, y_position, 0, 0)
        
        #Section
        base_lines = [
            create_line(gear_center_x + gear_radius + 5, y_position + 10, gear_center_x + gear_radius + 5, y_position + 10, 0, depth),
            create_line(gear_center_x + gear_radius + 5, y_position + 10, gear_center_x + gear_radius + 5, y_position, depth, depth),
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position, depth, 0),
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position + 10, 0, 0)
        ]
        swept3 = create_swept(line4, base_lines)

class LowerCase:

    def __init__(self, gear_center_x, gear_center_y, gear_radius, depth):
        self.depth = depth
        self.gear_center_x = gear_center_x
        self.gear_center_y = gear_center_y
        self.gear_radius = gear_radius

        def create_line(x_start, y_start, x_end, y_end, depth_start, depth_end):
            return Line(x_start, y_start, depth_start, x_end, y_end, depth_end)

        def create_swept(main_line, base_lines):
            return Swept([main_line], base_lines)

        half_gear_radius = gear_radius * 0.5
        y_position = gear_center_y + half_gear_radius  # changed to plus for mirroring uppercase 

        # Create first swept object

        #Guide
        line1 = create_line(gear_center_x - gear_radius - 10, y_position, gear_center_x - gear_radius - 10, gear_center_y, 0, 0)  # Keep x, Change y
        arc_g1 = Arc(gear_center_x, gear_center_y, 0, (1, 0, 0), (0, 1, 0), gear_radius + 10, 180, 360)  # Change arc angle to negative for mirroring
        line2 = create_line(gear_center_x + gear_radius + 10, y_position, gear_center_x + gear_radius + 10, gear_center_y, 0, 0)  # Keep x, Change y
        
        #Section
        base_lines = [
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 15, y_position, 0, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 15, y_position, 0, depth)  # Keep x, Change y
        ]
        swept = Swept([line1, arc_g1, line2], base_lines)

        # Create second swept object

        #Guide
        line3 = create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 110, y_position, 0, 0)  # Keep x, Change y
        
        #Section
        base_lines = [
            create_line(gear_center_x - gear_radius - 5, y_position - 10, gear_center_x - gear_radius - 5, y_position - 10, 0, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position - 10, gear_center_x - gear_radius - 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position - 10, 0, 0)  # Keep x, Change y
        ]
        swept2 = create_swept(line3, base_lines)

        # Create third swept object

        #Guide
        line4 = create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 110, y_position, 0, 0)  # Keep x, Change y
        
        #Section
        base_lines = [
            create_line(gear_center_x + gear_radius + 5, y_position - 10, gear_center_x + gear_radius + 5, y_position - 10, 0, depth),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position - 10, gear_center_x + gear_radius + 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position - 10, 0, 0)  # Keep x, Change y
        ]
        swept3 = create_swept(line4, base_lines)


class Wall:

    def __init__(self, gear_center_x, gear_center_y, gear_radius, depth, thickness, toothlength) -> None:
        self.center_x = gear_center_x
        self.center_y = gear_center_y
        self.radius = gear_radius + 15
        self.depth = depth
        self.thickness = thickness
        self.toothlength = toothlength

        self.initForNX()
    
    def initForNX(self):
        front_upper_wall = Cylinder(self.center_x, self.center_y, self.depth, self.radius*2, self.thickness)
        back_upper_wall = Cylinder(self.center_x, self.center_y,- self.thickness, self.radius*2, self.thickness)

        front_lower_wall = Cylinder(self.center_x, self.center_y-2 * self.radius  + 0.5*self.toothlength, self.depth, self.radius*2, self.thickness)
        back_lower_wall = Cylinder(self.center_x, self.center_y-2 * self.radius + 0.5*self.toothlength,- self.thickness, self.radius*2, self.thickness)
