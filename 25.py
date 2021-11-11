def f(x):
    pr = 1
    dels = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            dels.add(i)
            dels.add(x//i)
    if len(dels) < 5:
        return False
    else:
        dels = sorted(dels)[:5]
        for i in dels: pr *= i
    return pr

c = []
x = 200000001
while len(c) < 5:
    pr = f(x)
    if 0 < pr < x:
        print(pr)
        c.append(x)
    x += 1