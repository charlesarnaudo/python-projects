import datetime

name = input("What is your name?: ")
age = int(input("what is your age?: "))
year = datetime.datetime.now().year

print("Hi " + name + " you will be 100 in " + str((100 - age) + year))
