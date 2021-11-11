f = open('files/17.txt')
arr = [int(f.readline()) for _ in range(5542)]
k = k_max = 0
for i in range(len(arr)-1):
    e1 = arr[i]
    e2 = arr[i+1]
    if (e1%3 == 0 or e2%3 == 0) and ((e1+e2)% 5 == 0):
        k += 1
        k_max = max(k_max, e1+e2)
print(k, k_max)