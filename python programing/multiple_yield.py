def multiple_yield():
    str1 = "first"
    yield str1
    str2 = "secound"
    yield str2
    str3 = "third"
    yield str3
obj= multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
