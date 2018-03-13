import re

def re_up(s):
    print(s)
    line = s.rstrip()
    print(line)
    if re.search('^From:', s) == True:
        print(23)
    else:
        print(45)
re_up("From My name is From the alps in Swissland From")

