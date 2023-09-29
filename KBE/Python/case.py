import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\TMM4270-Automatisering\KBE\Python")
##

from Shapes.Swept import Swept 
from Shapes.Line import Line 
from Shapes.Arc import Arc

class Case:


    def __init__(self, gear_center_x, gear_center_y, gear_radius, depth):
        self.depth = depth
        self.gear_center_x = gear_center_x
        self.gear_center_y = gear_center_y
        self.gear_radius = gear_radius

        line1 = Line(gear_center_x - gear_radius - 10,gear_center_y - gear_radius*0.5,0,gear_center_x - gear_radius - 10, gear_center_y,0)
        arc_g1 = Arc(gear_center_x, gear_center_y,0,(1,0,0),(0,1,0),gear_radius + 10,0, 180)
        line2 = Line(gear_center_x + gear_radius + 10, gear_center_y - gear_radius*0.5,0,gear_center_x + gear_radius + 10,gear_center_y,0)

        base_line1 = Line(gear_center_x - gear_radius - 15, gear_center_y - 0.5*gear_radius, depth, gear_center_x - gear_radius - 5,gear_center_y - 0.5*gear_radius, depth)
        base_line2 = Line(gear_center_x - gear_radius - 5,gear_center_y - 0.5*gear_radius, depth, gear_center_x - gear_radius - 5,gear_center_y - 0.5*gear_radius,0)
        base_line3 = Line(gear_center_x - gear_radius - 5,gear_center_y - 0.5*gear_radius,0,gear_center_x - gear_radius - 15,gear_center_y - 0.5*gear_radius,0)
        base_line4 = Line(gear_center_x - gear_radius - 15,gear_center_y - 0.5*gear_radius,0, gear_center_x - gear_radius - 15,gear_center_y - 0.5*gear_radius, depth)

        swept = Swept([line1, arc_g1, line2], [base_line1,base_line2,base_line3,base_line4])

        line3 = Line(gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5,0,gear_center_x - gear_radius -110, gear_center_y - gear_radius*0.5,0)

        base_line1 = Line(gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5 + 10,0,gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5 + 10,depth)
        base_line2 = Line(gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5 + 10,depth,gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5,depth)
        base_line3 = Line(gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5,depth,gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5,0)
        base_line4 = Line(gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5,0,gear_center_x - gear_radius -5,gear_center_y - gear_radius*0.5 + 10,0)

        swept2 = Swept([line3], [base_line1,base_line2,base_line3,base_line4])

        # line4 = Line(110,-50,0,210,-50,0)

        # base_line1 = Line(105,-40,0,105,-40, depth)
        # base_line2 = Line(105,-40, depth,105,-50, depth )
        # base_line3 = Line(105,-50, depth,105,-50,0)
        # base_line4 = Line(105,-50,0,105,-40,0)

        # swept3 = Swept([line4], [base_line1,base_line2,base_line3,base_line4])

    # def __init__(self, x, y, z):

    #     line1 = Line(-110,-50,0,-110,0,0)
    #     arc_g1 = Arc(0,0,0,(1,0,0),(0,1,0),110,0, 180)
    #     line2 = Line(110,-50,0,110,0,0)

    #     base_line1 = Line(-115,-50,40,-105,-50,40)
    #     base_line2 = Line(-105,-50,40,-105,-50,0)
    #     base_line3 = Line(-105,-50,0,-115,-50,0)
    #     base_line4 = Line(-115,-50,0,-115,-50,40)

    #     swept = Swept([line1, arc_g1, line2], [base_line1,base_line2,base_line3,base_line4])

    #     line3 = Line(-105,-50,0,-210,-50,0)

    #     base_line1 = Line(-105,-40,0,-105,-40,40)
    #     base_line2 = Line(-105,-40,40,-105,-50,40)
    #     base_line3 = Line(-105,-50,40,-105,-50,0)
    #     base_line4 = Line(-105,-50,0,-105,-40,0)

    #     swept2 = Swept([line3], [base_line1,base_line2,base_line3,base_line4])

    #     line4 = Line(110,-50,0,210,-50,0)

    #     base_line1 = Line(105,-40,0,105,-40,40)
    #     base_line2 = Line(105,-40,40,105,-50,40)
    #     base_line3 = Line(105,-50,40,105,-50,0)
    #     base_line4 = Line(105,-50,0,105,-40,0)

    #     swept3 = Swept([line4], [base_line1,base_line2,base_line3,base_line4])

        #swept.unite(swept2)

