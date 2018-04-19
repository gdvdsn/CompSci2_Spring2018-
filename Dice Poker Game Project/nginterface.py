from ngraphics import Point
from ngraphics import Text
from nbutton import Button
from ndieview import DieView
from ngraphics import GraphWin

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Blackjack", 600, 400)
        self.win.setBackground("green3")

        banner = Text(Point(300,30), "Black Jack!")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        self.bjscore = 0
        b = Button(self.win, Point(300, 280), 150, 40, str(self.bjscore))
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []

        for i in range(2):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)

        for i in range(1,3):
            label = "Die %d" % (i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        self.money.setText("$%d" % (amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "%s! You win $%d" % (msg, score)
        else:
            text = "You rolled %s" % (msg)

        self.msg.setText(text)

    def setDice(self, values):
        for i in range(2):
            self.dice[i].setValue(values[i])
            self.bjscore += values[i]
            print(self.bjscore)

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = [] # No dice chosen yet

        while 1:
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
            "Roll Dice", "Score"])

            if b[0] == "D": # User clicked a die button
                i = eval(b[4]) - 1 # Translate label to die index

                if i in choices: # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")

                else: # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else: # User clicked Roll or Score
                for d in self.dice: # Revert appearance of all dice
                    d.setColor("black")

                if b == "Score": # Score clicked, ignore choices
                    return []

                elif choices != []: # Don’t accept Roll unless some
                    return choices # dice are actually selected

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while 1:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # function exit here.

    def close(self):
        self.win.close()

# = input("adad")
