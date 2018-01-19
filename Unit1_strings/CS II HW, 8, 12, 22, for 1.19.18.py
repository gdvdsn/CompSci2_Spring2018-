###Gabe Davidson
###Chapter 9, exercises 8, 12, 22

choice = input("1, 2, 3: ")

#8
def remove_char():
    s = input("Input string: ")
    remove_chr = input("Letter to remove from string: ")

    new_s = ""

    for achar in s:
        if achar != remove_chr:
            new_s += achar

    print(new_s)

def remove_str():
    s = input("Input string: ")
    remove_str = input("Word to remove from string: ")

    if s[len(s) - 1] != " ":
        s += " "

    check = ""
    new_str = ""

    for astring in s:
        if astring != " ":
            check += astring
        elif astring == " ":
            if check == remove_str:
                check = ""
            else:
                new_str += check + " "
                check = ""

    print(new_str)

def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: ${:.2f}'.format(total))
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total ${:.2f}'.format(total))
    print('Average price per item: ${:.2f}'.format(average))

if choice == "1":
    remove_char()
elif choice == "2":
    remove_str()
elif choice == "3":
    checkout()
