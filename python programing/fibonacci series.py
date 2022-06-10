def fun(d):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,d):
        c=a+b
        a=b
        b=c
        print(c)

l1=int(input("enter range of fibonacci series"))
fun(l1)
























