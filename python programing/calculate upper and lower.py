s='Sagar Mahjan'
def test(s):
    countu = 0
    countl = 0
    for c in s :
        if (c.isupper()):
            countu+=1
        if(c.islower()):
            countl+=1
    print("upper latter are",countu ," and lower latter are",countl)
test(s)
