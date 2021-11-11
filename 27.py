f = open('files/27-B.txt')
s = max_sum = 0
pr_sum = [float('inf')]*10
chetnye = 0
n = int(f.readline())

for i in range(n):
    x = int(f.readline())
    s += x
    if x%2 == 0: chetnye += 1
    if chetnye%10 == 0: max_sum = s

    elif pr_sum[chetnye%10] != float('inf'):
        max_sum = max(max_sum, s - pr_sum[chetnye%10])

    pr_sum[chetnye%10] = min(pr_sum[chetnye%10], s)
print(max_sum)