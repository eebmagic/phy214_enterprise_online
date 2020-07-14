import math

class point:
    def __init__(self, charge, position):
        self.charge = charge
        self.position = position


def force(k, q1, q2, r):
    numerator = k * (abs(q1 * q2))
    denom = r * r

    return numerator / denom


def dist(x1, x2):
    return abs(x2 - x1)


def point_force(x, y, k):
    d = dist(x.position, y.position)
    return force(k, x.charge, y.charge, d)


k = 8.988 # K constant
nanoMultiplier = 1e-9

a = point(5*nanoMultiplier, 0)
b = point(-5*nanoMultiplier, 2)
c = point(-3*nanoMultiplier, 4)

print(point_force(a, b, k))
print(point_force(b, c, k))

for i in range(11):
    b.charge += nanoMultiplier
    left = point_force(a, b, k)
    right = point_force(b, c, k)

    if round(left, 18) == round(right, 18):
        print(f"equal force: left: {left} right: {right}")
        print(f"    center charge: {b.charge}")
    else:
        print(f"center charge: {b.charge}, {left, right}")


print("\n\n")
a = point(5*nanoMultiplier, 0)
b = point(0, 2)
c = point(-3*nanoMultiplier, 4)

print(point_force(a, b, k))
print(point_force(b, c, k))