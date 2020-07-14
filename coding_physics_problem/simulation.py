import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class sphere:
    def __init__(self, pos, mass):
        self.position = pos
        self.mass = mass
        self.velocity = 0
        self.x_vector = 0
        self.y_vector = 0
        self.charge = 0


    def info(self):
        return(f"I am a sphere at: {self.position}, with mass: {self.mass} grams")


    def move(self):
        '''Moves the sphere by the direction vectors at spheres current velocity.
        Should be done once every second.'''
        newX = self.position[0] + (self.velocity * self.x_vector)
        newY = self.position[1] + (self.velocity + self.y_vector)
        self.position = (newX, newY)
        print(f"new position: {self.position}")


def get_force(k, q1, q2, r):
    F = (k * abs(q1 * q2)) / (r * r)
    return F


def distance(a, b):
    x_diff = a[0] - b[0]
    y_diff = a[1] - b[1]
    return math.sqrt((x_diff ** 2) + (y_diff ** 2))


k = 8.988 * (10 ** 9)

a = sphere((0, 0), 8.55)
b = sphere((0.15, 0), 8.55)

a.x_vector = -1
b.x_vector = 1
a.y_vector = 0
b.y_vector = 0

a.charge = 2.2899490873008303e-06
b.charge = 2.2899490873008303e-06


# Calculate first 100 positions
a_positions = []
b_positions = []

counter = 0
while counter < 100:
    # plot current positions
    a_positions.append(a.position)
    b_positions.append(b.position)

    # calculate forces and adjust object values
    repulsion = get_force(k, a.charge, b.charge, distance(a.position, b.position))
    a.velocity = repulsion
    b.velocity = repulsion

    # move objects
    a.move()
    b.move()

    counter += 1

print(f"a_positions: {a_positions}")
print(f"b_positions: {b_positions}")


print("\nStarting animation:")
width = 10

fig = plt.figure()
plt.xlim(-width, width)
plt.ylim(-width, width)
graph, = plt.plot([], [], 'o')

def animate(i):
    global a_positions
    global b_positions
    print(f"frame: {i}")
    graph.set_data(a_positions[i][0], a_positions[i][1])
    graph.set_data(b_positions[i][0], b_positions[i][1])
    return graph

ani = animation.FuncAnimation(fig, animate, frames=counter-1, interval=1000)
plt.show()
