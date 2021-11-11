for i in range(200, 300):
    s_sourced = '1'*i
    s = s_sourced
    while '111' in s or '222' in s:
        s = s.replace('111','22', 1)
        s = s.replace('222','1', 1)
    if s.count('2') == 0: print(len(s_sourced))