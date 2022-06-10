def div(a,b):
    print(a/b)
def sdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=sdiv(div)
div(2,4)