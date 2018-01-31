import turtle

def createLSystem28(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString28(startString)
        startString = endString

    return endString

def createLSystem29(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString29(startString)
        startString = endString

    return endString

def processString28(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules28(ch)

    return newstr

def processString29(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules29(ch)

    return newstr

def applyRules28(ch):
    newstr = ""
    if ch == 'H':
        newstr = 'HFX[+H][-H]'   # Rule 1
    elif ch == 'X':
        newstr = 'X[-FFF][+FFF]FX'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def applyRules29(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F[-F]F[+F]F'    #rule 1
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    saved_position = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            saved_position.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
        elif cmd == ']':
            newInfo = saved_position.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])


def main():
    choice = input("28, 29")

    if choice == "28":
        inst = createLSystem28(4, "H")   # create the string
        print(inst)
        t = turtle.Turtle()            # create the turtle
        wn = turtle.Screen()
        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem(t, inst, 27.5, 5)  # draw the picture

        wn.exitonclick()

    elif choice == "29":
        inst = createLSystem29(10, "F")   # create the string
        print(inst)
        t = turtle.Turtle()            # create the turtle
        wn = turtle.Screen()
        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem(t, inst, 25, 5)  # draw the picture

        wn.exitonclick()

main()
