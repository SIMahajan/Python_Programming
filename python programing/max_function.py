def max_of_two(x,y):
    if(x>y):
        return x
    return y
def max_of_tree(a,b,c):
    return(max_of_two(a,max_of_two(b,c)))
print(max_of_tree(10,30,20))