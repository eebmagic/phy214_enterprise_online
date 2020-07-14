'''
A collection of functions using formulas related to projections through lenses
'''

def image_distance(object_distance, focal_distance):
    '''
    Returns the distance (cm) to the projected image
    Given the:
        distance to the object being projected (cm),
        focal distance of the lens (cm)

    Formula:
        1/f = 1/s + 1/s'
        s' = 1 / (1/f - 1/s)

        f: focal distance
        s: object distance
        s': projected image distance
    '''

    denom = 1/focal_distance - 1/object_distance
    s_prime = 1 / denom

    return s_prime


def image_height(object_height, object_distance, projection_distance):
    '''
    Returns the height (cm) of the projection of the object
    Given the:
        height to object (cm),
        distance to object (cm),
        distance to projection (cm)

    Formula:
        y' / y = -s' / s
        y' = (-s' / s) * y

        y: height of object
        y': height of projection
        s: distance to object
        s': distance to projection
    '''

    projection_height = (-projection_distance / object_distance) * object_height

    return projection_height


def focal_point(curvature_radius):
    '''
    Returns the focal distance (cm)
    Given the:
        radius of the curvature of the lens

    Formula:
        f = 1/2 * r

        f: focal distance (cm)
        r: radius of lens curvature (cm)
    '''
    return (1/2) * curvature_radius


def curve_radius(focal_dist):
    '''
    Returns the radius (cm) of the lens curvature
    Given the:
        focal_dist

    Formula:
        f = 1/2 * r
        r = 2 * f

        f: focal distance (cm)
        r: radius of lens curvature (cm)
    '''
    return 2 * focal_dist


if __name__ == "__main__":
    obj_dist = 30
    obj_height = 5
    focal_point = -25

    projection_dist = image_distance(obj_dist, focal_point)
    projection_height = image_height(obj_height, obj_dist, projection_dist)

    print(f"projection_dist: {projection_dist}")
    print(f"projection_height: {projection_height}")