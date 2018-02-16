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

    #for term in n_dic:
        #print(term, "  ", n_dic[term])

    print(n_dic)

def main():
    file = open("Unsorted Alice in Wonderland")
    w_out = open("Sorted Alice in Wonderland", "w")

    cleaned_data = clean(file)
    sorted_data = sort(cleaned_data)
    #print(sorted_data)

main()
