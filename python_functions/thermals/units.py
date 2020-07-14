
def celscius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def fahrenheit(celscius):
    return ((9 / 5) * celscius) + 32


def kelvin(celscius):
    return celscius + 273


def calories(joules):
    return joules * (1 / 4.186)


def joules(calories):
    return 4.186 * calories


if __name__ == "__main__":
    c = [-15, -10, -5, 0, 5, 10, 15, 20]
    f = [-30, 0, 30, 60, 90, 120]

    print("Celscius:")
    for x in c:
        print(x, fahrenheit(x))

    print("\nFahrenheit:")
    for x in f:
        print(x, celscius(x))

    print("\nKelvin:")
    for x in c:
        print(x, kelvin(x))


    print("\nJoules -> Calories:")
    print(25, calories(25))
    print("\nCalories -> Joules:")
    print(12, joules(12))