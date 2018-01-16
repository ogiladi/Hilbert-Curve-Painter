import turtle as t
from random import randint

# create the turtle object
def setTurtle(myTuple):
    t.up()
    t.setx(myTuple[0])
    t.sety(myTuple[1])
    t.setheading(myTuple[2])
    t.down()

# build the list of intstruction for the turtle: move forward, right, left, etc.
def make_fractal(iterations, axiom, target, replace, target2, replace2):
    state = axiom
    for i in range(iterations):
        nextState = ''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState

    return state

# paint the fractal curve while transitioning from one colour to another
# the default value for the start and end colours is the same
def paint_fractale(state, length, langle, rangle, color1=(33, 63, 112), color2=(33, 63, 112)):

    t.hideturtle()

    t.colormode(255)
    num_mvs = 0

    for move in state:
        if move == 'F':
            num_mvs += 1

    j = 0.0
    for move in state:
        if move == "F":
            new_color = ((1-j/num_mvs)*color1[0]+j/num_mvs*color2[0], (1-j/num_mvs)*color1[1]+j/num_mvs*color2[1], \
                       (1 - j / num_mvs) * color1[2] + j / num_mvs * color2[2])
            j += 1
            t.color(new_color)
            t.forward(length)
        elif move == "-":
            t.left(langle)
        elif move == "+":
            t.right(rangle)

# main function. asks the user for the number of iterations the length of
# the forward movement
if __name__ == '__main__':
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))

    t.speed(0)
    w = myLen * (2 ** iterations - 1)

    t.setup(width=w, height=w, startx=0, starty=0)
    setTurtle((-t.window_width() / 2, t.window_height() / 2, 0))
    t.setup(width=w * 2, height=w * 2, startx=0, starty=0)

    # Hilbert Curve
    state = make_fractal(iterations, 'L', 'L', '+RF-LFL-FR+', 'R', '-LF+RFR+FL-')
    paint_fractale(state, myLen, 90, 90)

    window = t.Screen()
    canvas = window.getcanvas()
    canvas.postscript(file='hilbert_curve')
