### basic code to import a text file into a program

#Write a function that implements a substitution cipher.
#In a substitution cipher one letter is substituted for
#another to garble the message. For example A -> Q,
#B -> T, C -> G etc. your function should take two
#parameters, the message you want to encrypt, and a
#string that represents the mapping of the 26 letters
#in the alphabet. Your function should return a string
#that is the encrypted version of the message.

def change_text(f):
    sub_let = input("Input character to replace followed by the character which will take its place: "
                    "\n(i.e. 'A B' will replace all A's with B's. '7 KL' will replace all 7's wil KL's):\n")

    while len(sub_let) < 3:
        sub_let = input("That is invalid, please input again: \n")

    for x in range(len(f)):
        if f[x] == sub_let[0]:
            f[x] == sub_let[2]

    return f

file = open("guido_vonRossum_speech.txt", "r")

data = file.read()

data = change_text(data)

print(data)
