div = int(input("What is your num?: "))

a = range(1, div)

for num in a:
    if div % num is 0:
        print(num)
