import turtle


def find_angle(number_sides):
    """
    This function calculates the angle that is used to turn the pen when drawing a polygon.
    :param number_sides: The number of sides in the polygon.
    :return: The angle.
    """
    return 180 - (((number_sides - 2)*180) / number_sides)


def draw_polygon():
    """
    Draw a polygon by asking the user how many sides, and the length of each side.
    """
    # Ask the user how many sides they want.
    number_sides = int(input("How many sides? "))
    # Ask the user how long they want the sides to be.
    length = int(input("How long is each side? "))

    # Calculate the turn angle for the polygon.
    turn_angle = find_angle(number_sides)
    screen = turtle.Screen()
    pen = turtle.Turtle()
    # Move the pen the length of the side, then turn the angle.
    # Then repeat for as many sides as requested.
    for i in range(0, number_sides):
        pen.forward(length)
        pen.left(turn_angle)
    input("Hit enter to quit ...")
    screen.bye()


def draw_points():
    """
    Ask the user for coordinates and draw a shape from them.
    """
    points = []
    finished = False
    # Ask the user for coordinates.
    while not finished:
        user_input = input("Enter a coordinate 'x,y' or enter 'z' if done. ")
        if user_input == "z":
            finished = True
        else:
            x, y = user_input.split(",")
            points.append((int(x), int(y)))

    # If no points were put in, then quit.
    if not points:
        return

    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.up()

    # Move the pen to the location of the first point.
    first_point = points.pop(0)
    pen.goto(first_point)
    pen.down()
    points.append(first_point)

    # Move the pen to each point to draw the figure.
    for x, y in points:
        pen.goto(x, y)

    input("Hit enter to quit ...")
    screen.bye()


def main():
    print("Let's draw a polygon!")
    print("Type 1 and hit enter to specify number of sides and side length.")
    print("Type 2 and hit enter to specify points on the coordinate plane.")
    choice = input("What would you like to do? ")
    if choice == "1":
        # The user selected one so draw a polygon.
        draw_polygon()
    else:
        # The user selected two so draw with points.
        draw_points()


if __name__ == "__main__":
    main()

