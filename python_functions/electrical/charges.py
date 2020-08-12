

def force(q1, q2, r):
    k = 8.99 * (10 ** 9)
    out = k * ((abs(q1) * abs(q2)) / (r ** 2))

    return out


def g_force(m1, m2, r):
    G = 6.674 * (10 ** -11)
    out = G * ((m1 * m2) / (r ** 2))

    return out




if __name__ == "__main__":
    e = 1.602 * (10 ** -19)
    r = 5.3 * (10 ** -11)
    m1 = 9.11 * (10 ** -31)
    m2 = 1.67* (10 ** -27)

    print(force(e, e, r))
    print(g_force(m1, m2, r))