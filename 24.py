f = open('files/24.txt').readline()
arr = [len(s) for s in f.split('A')]
k_max = 0
for i in range(len(arr)-1):
    e1, e2 = arr[i], arr[i+1]
    k_max = max(k_max, e1+e2+1)
print(k_max)