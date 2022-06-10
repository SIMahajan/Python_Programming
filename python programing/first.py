#687954321
#87954321
#7954321
#954321
#54321
#4321
#321
#21
#1
n=10
for i in range(0,n-1):
    for j in range(1,n):
        if((n-j)==9):
            print("6",end='')
        elif((n-j)==6):
            print("9",end='')
        else:
            print(n-j,end='')
    n=n-1
    print("")