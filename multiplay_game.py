import random
tp=int(input("total players: "))
p=[0 for i in range(tp)]
score=[0 for i in range(tp)]
stop=0
winner=0
xyz=1
while True:
    for x in range(tp):
        p[x]='player'+str(x+1)
        confirm=input('do you wanna play '+p[x]+' (hit enter): ')
        if confirm=='':
            num=random.randint(1,6)
            print('you rolled ',num)
            score[x]=score[x]+num
            if score[x]>=100:
                winner=x
                stop=1
                break
    print(f"{xyz} 's round is finish!")
    if stop==1:
        break

    con=input('do you wanna play another round?(y/n)')
    xyz+=1
    if con.lower()=='y':
        continue
    else:
        break

print('the winner is',p[winner])
print(p[winner],"'s score is ",score[winner])