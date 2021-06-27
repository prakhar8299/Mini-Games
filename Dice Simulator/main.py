import random
again = True

while again:
    print(random.randint(1,6))
    another_roll= input("Want to roll the dice again? (Y/N): ")
    if another_roll.upper() == 'Y':
        continue
    elif another_roll.upper() == 'N':
        break
    else:
        print("Incorrect response \n Y = Yes \n N = No\n")
        break
        