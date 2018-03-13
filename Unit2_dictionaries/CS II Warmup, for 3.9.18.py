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

    return new_string.lower()

def separate(s):
    dic = {}

    for line in s:
        for word in line.split():
            if word not in dic:
                dic[word] = s.count(word)

    return dic

def main():
    text = open("guido_vonRossum_speech(2).txt")
    ss = clean(text)
    sss = separate(ss)
    print(ss)

main()
