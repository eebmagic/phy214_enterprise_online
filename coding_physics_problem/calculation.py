import math

'''
21.11
Two very small 8.55-g spheres, 15.0 cm apart from center to center,
are charged by adding equal numbers of electrons to each of them.

Disregarding all other forces,
how many electrons would you have to add to each sphere
so that the two spheres will accelerate at 25.0g when released?
Which way will they accelerate?

Force formula with Coulomb charges:
    
    F = (k * |q1 * q2|) / (r * r)

    k = 8.988 * (10 ** 9)
    in: (N * m^2) / (C^2)


g = 9.8 m/s^2
25g = 245 m/s^2

F (in Newtons) = mass * acceleration
F = 0.00855 kilograms * 245 m/s^2
'''

def get_q2(F, k, r):
    return (F * (r * r)) / k


def get_force(k, q1, q2, r):
    F = (k * abs(q1 * q2)) / (r * r)
    return F


Force = 0.00855 * 245
k = 8.988 * (10 ** 9)
radius = 0.15

charge_per_electron = -1.6 * (10 ** -19)

necessary_charge = math.sqrt(get_q2(Force, k, radius))

electrons = abs(necessary_charge / charge_per_electron)

resulting_force = get_force(k, necessary_charge, necessary_charge, radius)


print(necessary_charge)
print(electrons)
print(resulting_force)


