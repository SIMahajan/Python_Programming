def reverce(s):
    str=""
    for ele in s:
        str =  ele + str
    return str
s='sagar mahajan'
print(reverce(s))