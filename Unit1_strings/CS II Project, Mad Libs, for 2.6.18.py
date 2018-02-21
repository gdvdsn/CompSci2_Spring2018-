show_libs = open("CS II Project, text, for 2.6.18 (mad libs) (1)", "r")
edit_libs = open("CS II Project, text, for 2.6.18 (mad libs) (2)", "r")

def make_libs(show, edit):
    n_lib = []
    s_libs = show.read()

    print(s_libs + "\n\n")

    for line in edit:
        e_lib = input(line + "Input Word(s): ")
        n_lib.append(line + e_lib)

    user_lib = " ".join(n_lib)

    for word in user_lib:
        print(word)
        if word == "_":
            user_lib = user_lib.replace("_", "", 1)
        elif word == "(n)" or word == "(family member)" or word == "(emotion)" or word == "(v)" or word == "(size)":
            user_lib = user_lib.replace(word, "", 1)

    print(user_lib)

def rev_make_libs(show, edit):
    dic = {}
    s_libs = show.read()

    counter = 0

    for line in edit:
        e_lib = input(line + "Input Word(s): ")
        dic[str(counter)] = e_lib
        counter += 1

    for k in dic:
        s_libs = s_libs.replace("___", dic[k], 1)

    for l in s_libs:
        if l == "(n)" or l == "(family member)" or l == "(emotion)" or l == "(v)" or l == "(size)":
            s_libs = s_libs.replace(l, "", 1)

    print(s_libs)

rev_make_libs(show_libs, edit_libs)
