import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\TMM4270-Automatisering\KBE\Python")
##

from Shapes.Swept import Swept 
from Shapes.Line import Line 
from Shapes.Arc import Arc

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
        line1 = create_line(gear_center_x - gear_radius - 10, y_position, gear_center_x - gear_radius - 10, gear_center_y, 0, 0)
        arc_g1 = Arc(gear_center_x, gear_center_y, 0, (1, 0, 0), (0, 1, 0), gear_radius + 10, 0, 180)
        line2 = create_line(gear_center_x + gear_radius + 10, y_position, gear_center_x + gear_radius + 10, gear_center_y, 0, 0)
        base_lines = [
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 5, y_position, depth, depth),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 15, y_position, 0, 0),
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 15, y_position, 0, depth)
        ]
        swept = Swept([line1, arc_g1, line2], base_lines)

        # Create second swept object
        line3 = create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 110, y_position, 0, 0)
        base_lines = [
            create_line(gear_center_x - gear_radius - 5, y_position + 10, gear_center_x - gear_radius - 5, y_position + 10, 0, depth),
            create_line(gear_center_x - gear_radius - 5, y_position + 10, gear_center_x - gear_radius - 5, y_position, depth, depth),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position + 10, 0, 0)
        ]
        swept2 = create_swept(line3, base_lines)

        # Create third swept object
        line4 = create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 110, y_position, 0, 0)
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
        y_position = gear_center_y + half_gear_radius  # changed to plus for mirroring

        # Create first swept object
        line1 = create_line(gear_center_x - gear_radius - 10, y_position, gear_center_x - gear_radius - 10, gear_center_y, 0, 0)  # Keep x, Change y
        arc_g1 = Arc(gear_center_x, gear_center_y, 0, (1, 0, 0), (0, 1, 0), gear_radius + 10, 180, 360)  # Change arc angle to negative for mirroring
        line2 = create_line(gear_center_x + gear_radius + 10, y_position, gear_center_x + gear_radius + 10, gear_center_y, 0, 0)  # Keep x, Change y
        base_lines = [
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 15, y_position, 0, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 15, y_position, gear_center_x - gear_radius - 15, y_position, 0, depth)  # Keep x, Change y
        ]
        swept = Swept([line1, arc_g1, line2], base_lines)

        # Create second swept object
        line3 = create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 110, y_position, 0, 0)  # Keep x, Change y
        base_lines = [
            create_line(gear_center_x - gear_radius - 5, y_position - 10, gear_center_x - gear_radius - 5, y_position - 10, 0, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position - 10, gear_center_x - gear_radius - 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x - gear_radius - 5, y_position, gear_center_x - gear_radius - 5, y_position - 10, 0, 0)  # Keep x, Change y
        ]
        swept2 = create_swept(line3, base_lines)

        # Create third swept object
        line4 = create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 110, y_position, 0, 0)  # Keep x, Change y
        base_lines = [
            create_line(gear_center_x + gear_radius + 5, y_position - 10, gear_center_x + gear_radius + 5, y_position - 10, 0, depth),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position - 10, gear_center_x + gear_radius + 5, y_position, depth, depth),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position, depth, 0),  # Keep x, Change y
            create_line(gear_center_x + gear_radius + 5, y_position, gear_center_x + gear_radius + 5, y_position - 10, 0, 0)  # Keep x, Change y
        ]
        swept3 = create_swept(line4, base_lines)


