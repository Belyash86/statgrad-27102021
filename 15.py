def f(a):
    k = 0
    for x in range(10000):
            if x&85 != 0 or (x&54 == 0 or x&a != 0):
                k += 1
    if k == 10000: return True
    return False

for a in range(1000):
    if f(a):
        print(a)
        break