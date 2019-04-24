#random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if _name_=="_main_":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))