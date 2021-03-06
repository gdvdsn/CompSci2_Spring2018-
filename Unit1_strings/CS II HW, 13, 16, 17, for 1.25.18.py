###Gabe Davidson
###Chapter 9, exercises 13, 16, 17

import turtle

def createLSystem13(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString13(startString)
        startString = endString

    return endString

def createLSystem14(numIters,axiom):
   # print("createLSystem14 check")
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString14(startString)
        startString = endString

    return endString

def createLSystem17(numIters,axiom):
   # print("createLSystem14 check")
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString17(startString)
        startString = endString

    return endString

def processString13(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules13(ch)

    return newstr

def processString14(oldStr):
   # print("ProcessString14 check")
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules14(ch)

    return newstr

def processString17(oldStr):
   # print("ProcessString14 check")
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules17(ch)

    return newstr

def applyRules13(ch):
    newstr = ""
    if ch == 'L':
        newstr = '+RF-LFL-FR+'   # Rule 1
    elif ch == 'R':
        newstr = '-LF+RFR+FL-'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def applyRules14(ch):
   # print("applyRules14 check")
    newstr = ""
    if ch == 'X':
        print(3)
        newstr = 'X+YF+'   # Rule 1
    elif ch == 'Y':
        newstr = '-FX-Y'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def applyRules17(ch):
   # print("applyRules14 check")
    newstr = ""
    if ch == 'F':
        print(3)
        newstr = 'FF'   # Rule 1
    elif ch == 'X':
        newstr = '--FXF++FXF++FXF--'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem13(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def drawLsystem14(aTurtle, instructions, angle, distance):
   # print("drawLSystem14 check")
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def drawLsystem17(aTurtle, instructions, angle, distance):
   # print("drawLSystem14 check")
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    choice = input("13, 14, or 17: ")

    if choice == "13":
        inst = createLSystem13(4, "R")   # create the string
        print(inst)
        t = turtle.Turtle()            # create the turtle
        wn = turtle.Screen()

        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem13(t, inst, 105, 5)   # draw the picture
                                      # angle 60, segment length 5
        wn.exitonclick()

    elif choice == "14":
        print(333)
        inst = createLSystem14(10, "X")   # create the string
        print(inst)
        t = turtle.Turtle()            # create the turtle
        wn = turtle.Screen()

        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem14(t, inst, 90, 5)   # draw the picture
                                      # angle 60, segment length 5
        wn.exitonclick()

    elif choice == "17":
        print(333)
        inst = createLSystem17(4, "FXF--FF--FF")   # create the string
        print(inst)
        t = turtle.Turtle()            # create the turtle
        wn = turtle.Screen()

        t.up()
        t.back(200)
        t.down()
        t.speed(9)
        drawLsystem17(t, inst, 60, 5)   # draw the picture
                                      # angle 60, segment length 5
        wn.exitonclick()

main()
