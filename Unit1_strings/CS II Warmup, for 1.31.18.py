import string

file = open("guido_vonRossum_speech.txt", "r")

data = file.read()

def each_word_(text):
    new_text = ""

    for l in text:
        if l not in string.punctuation:
            new_text += l

    new_text.lower()

    all_words = new_text.split()
    unique_words = []

    for a in all_words:
        if a not in unique_words:
            unique_words.append(a)

    for b in range(len(unique_words)):
        num_b = text.count(str(unique_words[b]))

        print(str(unique_words[b] + ": " + str(num_b)))

each_word_(data)
