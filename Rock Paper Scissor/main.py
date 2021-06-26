import random
#importing random library
def gameWin(comp,you): #defining the gamewin function
    if comp == you:
        return None
    elif comp == 'r':
        if you== 'sc':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 'sc':
            return True
    elif comp == 'sc':
        if you == 'r':
            return True
        elif you == "p":
            return False

print("Comp Turn : Rock(r) OR Paper(p) OR Scissor(sc)")#letting computer to choose either rock or paper or scissor
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp ='p'
elif randNo == '3':
    comp = 'sc'
#print(randNo)

you= input ("Your Turn : Rock(r) Paper(p) or Scissor(sc)?") #input  from player
a = gameWin(comp,you)
#finalising the winner
print(f"Computer Chose {comp}")
print(f"You Choosed {you}")

if a== None:
    print("It,s a Tie!")
elif a:
    print ("You Win!")
else:
    print("You Lose!")