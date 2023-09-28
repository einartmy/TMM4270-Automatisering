import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\TMM4270-Automatisering\KBE\Python")
##
# from Shapes.Swept import Swept
# from Shapes.Line import Line
# from Shapes.Arc import Arc

# line = Line(0, 0, 0, 0, 0, 100)
# arc = Arc(0, 0, 0, (1, 0, 0), (0, 1, 1), 50, 0, 360)
# #
# swept = Swept([line], [arc])

#Example 2

from Shapes.Swept import Swept 
from Shapes.Line import Line 
from Shapes.Arc import Arc

line = Line(0,0,0,0,0,100)
arc_g1 = Arc(50,0,100,(1,0,0),(0,0,1),50,0, 180)
line = Line(100,0,0,100,0,100)

line1 = Line(-5,5,0,5,5,0)
line2 = Line(5,5,0,5,-5,0)
line3 = Line(5,-5,0,-5,-5,0)
line4 = Line(-5,-5,0,-5,5,0)

# swept = Swept([line, arc_g1],[line1,line2,line3,line4])

swept = Swept([line, arc_g1], [line1,line2,line3,line4])

