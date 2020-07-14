import turtle
import lenses
import time

def draw(position, height, focal_distance):
    # make turtle
    t = turtle.Turtle()
    t.speed('fastest')
    t.home()
    t.clear()

    # draw center of lens
    t.left(90)
    t.fd(100)
    t.back(200)
    t.fd(100)
    t.right(90)

    # draw axis
    t.fd(300)
    t.back(600)
    t.fd(300)

    # reset
    t.penup()
    t.home()
    t.pendown()

    # draw focii
    t.back(focal_distance * 10)
    t.circle(10)
    t.fd(focal_distance * 10 * 2)
    t.circle(10)

    # reset
    t.penup()
    t.home()
    t.pendown()

    # do math
    image_position = lenses.image_distance(position, focal_distance)
    image_height = lenses.image_height(height, position, image_position)

    # position = -position
    
    # draw object
    t.fd(position*10)
    t.left(90)
    t.fd(height*10)
    print(f"Object:\n\tposition: {position}\n\theight: {height}")
    
    # reset
    t.penup()
    t.home()
    t.pendown()

    # draw image
    t.fd(image_position * 10)
    t.left(90)
    t.fd(image_height * 10)
    print(f"\nImage:\n\tposition: {image_position}\n\theight: {image_height}")

    # reset
    t.penup()
    t.home()
    t.pendown()
    
    # wait
    # input("press enter to quit")
    # time.sleep(1)
    turtle.done()
    t.clear()


if __name__ == "__main__":
    draw(-7.03, 0.33, 12)
