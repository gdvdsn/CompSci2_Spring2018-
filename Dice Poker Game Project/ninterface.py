class TextInterface:
    def __init__(self):
        print("Welcome to video poker.")
    def setMoney(self, amt):
        print("You currently have $%d." % (amt))

    def setDice(self, values):
        print("Dice:", values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for playing!")

    def showResult(self, msg, score):
        print("%s. You win $%d." % (msg, score))

    def chooseDice(self):
        return input("Enter list of which to change ([] to stop) ")

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
