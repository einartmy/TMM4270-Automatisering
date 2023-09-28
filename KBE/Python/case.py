import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\TMM4270-Automatisering\KBE\Python")
##

from Shapes.Swept import Swept 
from Shapes.Line import Line 
from Shapes.Arc import Arc

line1 = Line(-110,-50,0,-110,0,0)
arc_g1 = Arc(0,0,0,(1,0,0),(0,1,0),110,0, 180)
line2 = Line(110,-50,0,110,0,0)



base_line1 = Line(-115,-50,5,-105,-50,5)
base_line2 = Line(-105,-50,5,-105,-50,-5)
base_line3 = Line(-105,-50,-5,-115,-50,-5)
base_line4 = Line(-115,-50,-5,-115,-50,5)

swept = Swept([line1, arc_g1, line2], [base_line1,base_line2,base_line3,base_line4])

line3 = Line(-105,-50,0,-210,-50,0)

base_line1 = Line(-105,-40,-5,-105,-40,5)
base_line2 = Line(-105,-40,5,-105,-50,5)
base_line3 = Line(-105,-50,5,-105,-50,-5)
base_line4 = Line(-105,-50,-5,-105,-40,-5)

swept2 = Swept([line3], [base_line1,base_line2,base_line3,base_line4])

line4 = Line(110,-50,0,210,-50,0)

base_line1 = Line(105,-40,-5,105,-40,5)
base_line2 = Line(105,-40,5,105,-50,5)
base_line3 = Line(105,-50,5,105,-50,-5)
base_line4 = Line(105,-50,-5,105,-40,-5)

swept2 = Swept([line4], [base_line1,base_line2,base_line3,base_line4])


