from Kitchenware.Elements.Body import Body
from Kitchenware.Elements.Lid import Lid

class Teapot:

    # Constructor of a teapot class
    def __init__(self, diameter, lid_dia, handle_radius, length_spout, knob_dia):
        self.diameter = diameter
        self.lid_dia = lid_dia
        self.handle_radius = handle_radius
        self.length_spout = length_spout
        self.knob_dia = knob_dia

        self.body = Body(diameter, (0, 0, 0), ((1,0,0), (0,1,0)))
        self.lid = Lid(lid_dia)

