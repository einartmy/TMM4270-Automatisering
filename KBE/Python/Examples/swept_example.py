import sys

##your path here
sys.path.append("M:\Desktop\TMM4270\KBE\Python")
##
from Shapes.Swept import Swept
from Shapes.Line import Line
from Shapes.Arc import Arc

line = Line(0, 0, 0, 0, 0, 100)
arc = Arc(0, 0, 0, (1, 0, 0), (0, 1, 1), 50, 0, 360)
#
swept = Swept([line], [arc])
