x = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
m = [0]*16
while x:
    m[x%16] += 1
    x //= 16

k = 0
for i in m:
    if i>0: k+=1
print(k)