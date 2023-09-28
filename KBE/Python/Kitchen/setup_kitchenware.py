from Kitchenware.Teapot import Teapot

t1 = Teapot(100, 41, 40, 25, 5)
t2 = Teapot(70, 42, 40, 25, 5)
t3 = Teapot(110, 43, 40, 25, 8)

teapots = [t1, t2, t3]

for t in teapots:
    print("Lid diameter", t.lid.dia)