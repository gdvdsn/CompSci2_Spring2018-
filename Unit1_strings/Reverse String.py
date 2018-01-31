def reverse(s):
    r_string = ""

    for x in range(len(s)):
        r_string += s[-x - 1]

    return r_string

astring = input("Input string: ")

reverse_string = reverse(astring)

print(reverse_string)
