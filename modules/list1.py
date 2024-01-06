#addin items into a list using the random module

import random

num = []
for i in range(5):
    num.append(random.randrange(1,5))
    print("{}".format(num),sep=",",end= " ")
