'''
A collection of functions using formulas related to light refractions through substances
'''
import math

# Constants
speed_of_light = 3 * (10 ** 8)

def refraction_index(speed_in_substance):
    '''
    Returns the unitless refraction index for a substance
    Given the:
        speed in m/s of light in the substance

    Formula:
        n = c/v
        
        n: index of refraction
        c: speed of light (3 * 10^8 m/s)
        v: speed in substance
    '''
    global speed_of_light

    index = speed_of_light / speed_in_substance

    return index


def speed_in_substance(refraction_index):
    '''
    Returns the speed of light through a substanec
    Given the:
        refraction index of that substance (unitless)
    
    Formula:
        n = c/v
        
        n: index of refraction
        c: speed of light (3 * 10^8 m/s)
        v: speed in substance
    '''
    global speed_of_light

    speed_in_substance = speed_of_light / refraction_index

    return speed_in_substance
    

def refraction_angle(theta1, n1, n2):
    '''
    Returns the angle of refraction in a substance
    (will return string "undefined" if angle would be greater than or equal 90 degrees)
    Given the:
        angle of incidence (degrees),
        refraction index before incidence with substance (unitless),
        refraction index after incidence with substance (unitless)

    Formula:
        n1 * sin(theta1) = n2 * sin(theta2)
        theta2 = sin^-1((n1 / n2) * sin(theta1))

        theta1: angle of incidence
        theta2: angle of refraction
        n1: refraction index before incidence (outside of substance)
        n2: refraction index after incidence (inside of substance)
    '''
    theta2 = "undefined"
    try:
        z = (n1 / n2) * math.sin(math.radians(theta1))
        theta2 = math.degrees(math.asin(z))
    except:
        pass
    return theta2


def index_from_angles(theta1, theta2, n1):
    '''
    Returns the refraction index of the substance
    Given the:
        angle of incedence (< 90 degrees),
        angle of refraction (< 90 degrees),
        refraction index before incidence (unitless)

    Formula:
        n1 * sin(theta1) = n2 * sin(theta2)
        n2 = (n1 * sin(theta1)) / sin(theta2)

        theta1: angle of incidence
        theta2: angle of refraction
        n1: refraction index before incidence (outside of substance)
        n2: refraction index after incidence (inside of substance)
    '''
    if theta1 >= 90 or theta2 >= 90:
        raise ValueError(f"Angles must be less than 90 degrees (passed: theta1 = {theta1}; theta2 = {theta2})")

    n2 = (n1 * math.sin(theta1)) / math.sin(theta2)
    return n2


### TODO ###
'''
def critical_angle(theta1, n1, n2):
    pass
'''

if __name__ == "__main__":
    # Speed and indexes
    glass_speed = 2.2 * (10 ** 8)
    glass_refraction_index = refraction_index(glass_speed)
    print(f"glass:\n\tspeed: {glass_speed}\n\trefraction index: {glass_refraction_index}")

    water_index = 1.33
    water_speed = speed_in_substance(water_index)
    print(f"\nwater:\n\tindex: {water_index}\n\tspeed: {water_speed}\n\n")


    # Angles
    ins = [15, 30, 35, 40, 41, 41.5, 42, 43, 55]
    n1 = 1.5
    n2 = 1

    for x in ins:
        print(x, refraction_angle(x, n1, n2))


    print("\nOther problem")
    print(refraction_angle(30, 1.33, 1.66))

    print("\nindex from angles: ")
    print(index_from_angles(30, 23.62, 1.33))