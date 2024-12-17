import random

user_wins=computer_wins=0
options=['p','s','r']
def picking(x):
    if x=='s':
        return "Scissors"
    elif x=='p':
        return "Paper"
    else:
        return "Rock"
while True:
    user_input=input("Paper(p) , Scissor(s) , Rock(r) or Quit(q) :").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("The Computer pick: ",picking(computer_pick),'.')
    
    if user_input == 'r' and computer_pick=='s':
        print('You Won !')
        user_wins+=1
    elif user_input == 'p' and computer_pick =='r':
        print('You Won !')
        user_wins+=1
    elif user_input == 's' and computer_pick =='p':
        print('You Won !')
        user_wins+=1
    else:
        print('You Lost !')
        computer_wins+=1
print("You won",user_wins,'Times.')
print("The Computer won",computer_wins,'Times.')
if user_wins>computer_wins:
    print("So you are the winner !!!")
elif computer_wins>user_wins:
    print("The Computer is the winner !!! ")
    print("Better luck next time.")
else:
    print("Match Tie!!!")
print("Good Bye")