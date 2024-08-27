s = "abciiidef"
k = 3

vowels = {'a', 'e', 'i', 'o', 'u'}

l, cnt, res = 0, 0, 0
for r in range(len(s)):     # 2 c
    
    if s[r] in vowels:
        cnt += 1
    else:
        0
    
    if r - l + 1 > k:
        if s[l] in vowels:
            cnt -= 1
        else:
            0
        l += 1
    res = max(res, cnt)
print(res)