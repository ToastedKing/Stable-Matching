#Generates test files for Project 1

from numpy import random

def generate_preferences(n):
    preference = random.permutation(list(range(1,n+1)))
    preference_string = ""
    for number in preference:
        preference_string = preference_string + str(number) + " "
    return preference_string[:-1] + "\n"

def create_test(name, n):
    f = open(name, "w+")
    for i in range(1,n+1):
        f.write(generate_preferences(n))
    f.write("\n")
    for i in range(1,n+1):
        f.write(generate_preferences(n))

create_test("test1.txt", 3)
create_test("test2.txt", 4)
create_test("test3.txt", 5)
create_test("test4.txt", 10)
