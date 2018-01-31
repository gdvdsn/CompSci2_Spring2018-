file = open("guido_vonRossum_speech.txt", "r")

data = file.read()

choice = input("1. to input message, then optional decrypt. 2. to decrypt pre-existing text: ")

if choice == "1":
    encryptedMessageString = input("Input message: ")

    #how many substitutions
    num_substitutions = int(input("\nHow many substitutions do you want to make? (Number cannot exceed the length of the message or number of unique characters within the message.)\n"))

    #set of unique characters within encryptedMessageString for 'y'
    num_unique_chars_encryptedMessageString_list = []
    num_unique_chars_encryptedMessageString_set = []

    for i in range(len(encryptedMessageString)):
        num_unique_chars_encryptedMessageString_list.append(chr(ord(encryptedMessageString[i])))
        num_unique_chars_encryptedMessageString_set = set(num_unique_chars_encryptedMessageString_list)

        #numSubstitutions invalid if...
    if (num_substitutions > (len(encryptedMessageString))) or (num_substitutions > (len(num_unique_chars_encryptedMessageString_list))):

        #numSubstitutions invalid if is > length of encryptedMessageString
        while(num_substitutions > len(encryptedMessageString)):
            num_substitutions = int(input("This number exceeds the length of your message. Please input a different integer.\n"))

            #numSubstitutions invalid if is > # of uniqe characters within encryptedMessageString
        while(len(encryptedMessageString)) > (len(num_unique_chars_encryptedMessageString_set)):
            num_substitutions = int(input("This number exceeds the length of unique characters within your message. Please input a different integer.\n"))

        #substitution inputs
    substitution_x = ""
    substitution_y = ""
    substitution_list_x = []
    substitution_list = []

    for j in range(num_substitutions):
        substitution_x = input("\nInput a character for 'x': \n")

        substitution_list_x.append(substitution_x)

        #y list
        print("And now for the corresponding 'y' character(s).\n")
        substitution_y = input("Input a corresponding character(s) for 'y': \n")

        if substitution_y not in substitution_list:
            substitution_list.append(substitution_y)
            encryptedMessageString = (encryptedMessageString.replace(substitution_x, substitution_y))

        else:
            contWhileLoop = True

            while contWhileLoop == True:
                substitution_y = input("You already have a substitution cipher for '" + substitution_y + ".' Please input a different character(s) for 'y'.'")

                if substitution_y in substitution_list:

                    break
                else:
                    substitution_list.append(substitution_y)
                    encryptedMessageString = (encryptedMessageString.replace(substitution_x, substitution_y))
                    contWhileLoop = False

    print(encryptedMessageString, "\n\n")

    choice2 = input("1. to decrypt encrypted message. 2. to end: ")

    if choice2 == "1":
        for i in range(len(substitution_x) + 1):
            for k in range(encryptedMessageString.count(substitution_list[i])):
                encryptedMessageString = encryptedMessageString.replace(substitution_list[i], substitution_list_x[i])

    print(encryptedMessageString)

elif choice == "2":
    #text = input("Input encrypted text: ")
    text = data

    substitution_num = int(input("How many substitutions were made in this encryption?: "))

    cipher_y = []
    cipher_x = []

    for k in range(substitution_num):
        ciph_y = input("Input character(s) to look for: ")
        cipher_y.append(ciph_y)

        ciph_x = input("Input character to replace said character(s) with (cannot be more than one character): ")

        cipher_x.append(ciph_x)

    for l in range(substitution_num):
        print(l, cipher_y, cipher_x)
        text = text.replace(cipher_y[l-1], cipher_x[l-1])

    print(text)
