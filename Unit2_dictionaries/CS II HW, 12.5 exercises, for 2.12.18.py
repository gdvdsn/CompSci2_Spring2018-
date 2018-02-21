import turtle

def count_all(string):
    dic = {}

    for letter in string:
        if letter not in dic:
            dic[letter] = string.count(letter)

    return dic

def find_largest(dic):
    largest = 0

    for x in dic:
        if int(dic[x]) > largest:
            largest = int(dic[x])

    return largest

def count_all_to_histo(old_dic):
    hold_list = []

    for k in old_dic:
        hold_list.append(k)

    hold_list.sort()

    dic = {}

    for h in hold_list:
        dic[h] = old_dic[h]

    largest = find_largest(dic)
    scale_actual = largest / 720

    aa = turtle.Turtle()
    win = turtle.Screen()
    win.tracer(0)
    win.setworldcoordinates(-400, -400, 400, 400)

    aa.penup()
    aa.goto(-390, -390)

    for x in dic:
        aa.setheading(0)
        aa.penup()
        aa.forward((800 / len(dic)) / 2)
        aa.pendown()
        if int(150 / len(dic)) > 7:
            aa.write(str(x), font=("Arial", int(150 / len(dic)), "normal"))
        else:
            aa.write(str(x), font=("Arial", 7, "normal"))
        if x == ' ':
            if int(150 / len(dic)) > 7:
                aa.write(str(x), font=("Arial", int(150 / len(dic)), "normal"))
            else:
                aa.write(str(x), font=("Arial", 7, "normal"))
        aa.right(180)
        aa.penup()
        aa.forward((800 / len(dic)) / 2)
        aa.setheading(90)
        aa.penup()
        aa.forward(30)
        aa.pendown()
        if largest < 750:
            aa.forward(int(dic[x]) * 30)
        else:
            aa.forward(int(dic[x]) / scale_actual)
        aa.penup()
        aa.forward(30)
        aa.right(90)
        aa.forward((800 / len(dic)) / 2)
        aa.pendown()
        if int(150 / len(dic)) > 7:
            aa.write(dic[x], font=("Arial", int(150 / len(dic)), "normal"))
        else:
            aa.write(dic[x], font=("Arial", 7, "normal"))
        aa.penup()
        aa.right(180)
        aa.forward((800 / len(dic)) / 2)
        aa.left(90)
        aa.forward(30)
        aa.pendown()
        aa.left(90)
        aa.forward(800 / len(dic) - (30 / len(dic)))
        aa.right(90)
        if largest < 750:
            aa.forward(int(dic[x]) * 30)
        else:
            aa.forward(int(dic[x]) / scale_actual)
        aa.penup()
        aa.forward(30)
        aa.pendown()

        win.update()

    win.exitonclick()

ss = input(":")

text = open("guido_vonRossum_speech(2).txt")
data = text.read()

letter_count = count_all(ss)
print(letter_count, len(letter_count))
count_all_to_histo(letter_count)
