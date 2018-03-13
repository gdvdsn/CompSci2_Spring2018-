import string

def clean(s):
    #gets punctuation
    punc = string.punctuation

    new_string = ""

    #for line
    for line in s:
        #for char in line
        for letter in line:
            #if its not in punc add it
            if letter not in punc:
                new_string += letter

    for line in new_string:
        sort(line)

    #return lowercase string, no punc
    return new_string.lower()

def sort(s):
    #create new dic
    n_dic = {}
    #for line in
    line_split = s.split()
    for word in line_split:
        if word not in n_dic:
            n_dic[word] = 1
        else:
            n_dic[word] += 1

    for k in range(len(s)):
        if s[k] in n_dic == True:
            del n_dic[s[k]]

    return n_dic

def main():
    try:
        file = open("Unsorted Alice in Wonderland")
    except FileNotFoundError:
        print("This file is not found!")

    try:
        w_out = open("Sorted Alice in Wonderland", "w")
    except FileNotFoundError:
        print("This second file is not found!")

    cleaned_data = clean(file)
    sorted_data = sort(cleaned_data)

    for h in sorted_data:
        w_out.write(str(w_out.write("{0}    :    {1}\n".format(h, sorted_data[h]))))

    print(w_out)

main()
