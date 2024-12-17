import time

t=int(input("enter time in seconds :"))
for x in range(t,-1,-1):
    time.sleep(1)
    sec=x%60
    min=(x//60)%60
    hours=(x//3600)%24
    print(f"{hours:02}:{min:02}:{sec:02}")