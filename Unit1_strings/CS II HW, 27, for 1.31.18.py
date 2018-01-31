###Gabe Davidson
###Unit 10, exercise 27

def replace_(string, old, new):
    r_string = ""
    word_list = string.split()

    for i in word_list:
        if i == old:
            r_string = r_string + new + " "
        else:
            r_string = r_string + i + " "

    return r_string

text = "Hello there my name is Habe Davidson"

new_text = replace_(text, "Habe", "Gabe")

print(text, "\n", new_text)
