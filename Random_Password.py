import random
import string
def create_pwd():
    password=''
    for x in range(5):
        picked_letter=random.choice(string.ascii_letters)
        password+=picked_letter
    special_characters=['@','!','#','$','&']
    password+=random.choice(special_characters)
    for x in range(3):
        password+=random.choice(string.digits)
    return password
x=create_pwd()
if (x[0:5]==x[0:5].lower()) or (x[0:5]==x[0:5].upper()):
    print(f"Your Genarated Password is: {create_pwd()}")
else:
    print(f"Your Genarated Password is: {x}")
