win = False

while(not win):
    p1 = input("Rock, Paper or Scissor? ")
    p2 = input("Rock, Paper or Scissor? ")

    p1 = p1.lower
    p2 = p2.lower

    if p1 == p2:
        print("They were the same!")
    elif p1 == 'rock':
        if u2 == 'scissor':
            print("p1 wins")
            win = True
        else:
            print("p2 wins")
