import random

def encrypt_6(s):
    new_string = ""

    s = s.lower()

    for j in range(len(s)):
        ord_val = ord(s[j])

        if ord_val >= 96 and ord_val <= 122:
            ord_val_2 = ord_val - 6

            if ord_val_2 < 96:
                ord_val_2 = ord_val - 96

                ord_val_2 = 122 - ord_val_2

            new_string += chr(ord_val_2)

        else:
            new_string += " "

    return new_string

def find_avg(n):
    num = 0

    for x in n:
        num += int(x)

    return num / len(n)

def longest_word(t):
    dic = {}
    ls = []

    for line in t:
        ls.extend(line.split())

    long = ""
    counter = 1
    for term in ls:
        dic[counter] = term
        counter += 1

        if len(term) > len(long):
            long = term

    if ord(long[len(long) - 1]) < 96 or ord(long[len(long) - 1]) > 122:
        long = long[:(len(long) - 1)]

    return_statement = ("The longest word  in the text is " + long + ". It is " + str(len(long)) + " characters long.")

    return return_statement

def main():
    #encrypt_6_string = encrypt_6("Hello World My Name Is Gabe Davidson")
    #print(encrypt_6_string)

    rand_num_list = []

    for k in range(100):
        rand_num_list.append(random.randint(0, 1000))

    #avg_rand_num_list = find_avg(rand_num_list)
    #print(avg_rand_num_list)

    text = open("CS II Test, text, on 2.21.18")

    #longest_word_word = longest_word(text)
    #print(longest_word_word)

main()
