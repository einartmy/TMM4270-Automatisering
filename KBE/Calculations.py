import math
radius = 0.1

x = 10
y = 200
caseThickness = 15


def numberOfTeeth(gearRadius, teethRadius):
        
        return math.ceil(2*gearRadius * math.pi * 0.5 * (1/teethRadius))


def vpm():
    depth = 2*radius
    teethradius = radius/5
    angleSpeed = 1
    teeths = numberOfTeeth(radius, teethradius)
    

    angle = 2*math.pi / teeths
    korde = ((radius + teethradius)**2 * math.sin(angle)) / 2
    areal = 4*teethradius**2 + korde #2teethradius * 2teethradius
    volume = areal*depth
    
    rpm = angleSpeed * 60 /(2*math.pi*radius)
    return volume*teeths*rpm*2

print(vpm())

def getPump(whishvpm):
      global radius 
      while whishvpm > vpm():
            
            radius += 0.02
            
      

getPump(20)
print(radius)


