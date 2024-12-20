import random

#● ┌ ─ ┐ │ └ ┘  these are the characters

dice_art={
  1:(
    "┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"
),2:(
    "┌─────────┐",
    "│  ●      │",
    "│         │",
    "│      ●  │",
    "└─────────┘"
),3:(
    "┌─────────┐",
    "│  ●      │",
    "│    ●    │",
    "│      ●  │",
    "└─────────┘"
),4:(
    "┌─────────┐",
    "│  ●   ●  │",
    "│         │",
    "│  ●   ●  │",
    "└─────────┘"
),5:(
    "┌─────────┐",
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │",
    "└─────────┘"
),6:(
    "┌─────────┐",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "└─────────┘"
)}
dice=[]
total=0
number_of_dice=int(input("How many dice:"))
for i in range(number_of_dice):
    dice.append(random.randint(1,6))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end='  ')#horizontally display
    print()

print(f"total is: {sum(dice)} ")
