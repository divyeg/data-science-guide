def canshift(a, b):
    a = list(a)
    b = list(b)
    i = 0
    while i in range(len(a)):
        num = a.pop()
        a.insert(0, num)
        if a == b:
            return True
        else:
            i += 1
    return False


a = "abc"
b = "acb"
print(canshift(a, b))
