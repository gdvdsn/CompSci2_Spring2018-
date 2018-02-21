import turtle

text = open("CS II HW, text, for 2.2.18 (student data).txt")
c_data = open("CS II HW, text, for 2.2.18 (turtle coords)")

def over_six_tests(data):
    for line in data:
        scores = line.split()
        #print(line, scores)

        if len(scores) > 7:
            print(" ".join(scores))

def avg_tests_score(data):
    for line in data:
        scores = line.split()

        print(scores)

        total_score = 0

        for x in range(len(scores[1:])):
            total_score += int(scores[x+1])

        avg_score = total_score/len(scores[1:])

        print(scores[0], avg_score)

def low_high_scores(data):
    for line in data:
        scores = line.split()

        num_list = []

        for x in range(len(scores[1:])):
            num_list.append(scores[x+1])

        low = int(num_list[1])
        high = int(num_list[1])

        for k in range(len(num_list)):
            if int(low) > int(num_list[k]):
                low = num_list[k]

            if int(high) < int(num_list[k]):
                high = num_list[k]

        print(scores[0], low, high)

def draw__(coords):
    aa = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-350, -350, 350, 350)

    for line in coords:
        go_to = line.split()

        if go_to[0] == "UP":
            print("up)")
            aa.penup()
        elif go_to[0] == "DOWN":
            print("down")
            aa.pendown()
        else:
            print(go_to)
            aa.goto(int(go_to[0]), int(go_to[1]))

    wn.exitonclick()

def main():
    choice = int(input("1, 2, 3, 5"))

    if choice == 1:
        over_six_tests(text)
    elif choice == 2:
        avg_tests_score(text)
    elif choice == 3:
        low_high_scores(text)
    elif choice == 5:
        draw__(c_data)

    text.close()
    c_data.close()

main()
