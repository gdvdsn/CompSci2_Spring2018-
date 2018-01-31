###Gabe Davidson
###Chapter 10, exercise 17

import random

num_list = []
num_avg = 0

for x in range(100):
    rand = random.randint(0, 1000)
    num_list.append(rand)
    num_avg += rand

print(num_list)
print("Average = " + str(num_avg/100))

