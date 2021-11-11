def avtomat(n):
    s = 0
    s_ch_mesta = 0
    for i in range(len(str(n))):
        d = int(str(n)[i])
        if d%2 == 0: s+=d
        if i%2 == 1: s_ch_mesta += d
    return abs(s-s_ch_mesta)

for n in range(1000):
    if avtomat(n) == 13:
        print(n)
        break