lst = [1, 2, 3, 4, 5, 1, 2]

# solution 1
new_lst = list(set(lst))
for i in range(len(lst)):
    if lst[i] in lst[i+1:]:
        new_lst.remove(lst[i])
print(new_lst)  # Output: [3, 4, 5]


# solution 2
new_lst2 = []
for i in lst:
    if lst.count(i) == 1:
        new_lst2.append(i)
print(new_lst2)  # Output: [3, 4, 5]


# solution 3
from collections import Counter

lst = [1, 2, 3, 4, 5, 1, 2]
count = Counter(lst)
new_lst = [x for x in lst if count[x] == 1]

print(new_lst)  # Output: [3, 4, 5]


# solution 4
count_dict = {}
for item in lst:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

new_lst = [item for item in lst if count_dict[item] == 1]

print(new_lst)  # Output: [3, 4, 5]

# Conclusion: The dictionary-based solutions 3 & 4 are much more efficient,
# reducing time complexity from 𝑂(𝑛2) to 𝑂(𝑛).

# solution 5
a = [1,2,3,4,5,1,2]
half_len = int(len(a)/2)
s = set(a[:half_len])
l = set(a[half_len:])
print(list(s ^ l))

