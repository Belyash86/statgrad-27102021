def f(start, end):
    if start > end: return False
    if start == end: return True
    return f(start+1, end) + f(start*3,end)

print(f(2,28)*f(28,90))