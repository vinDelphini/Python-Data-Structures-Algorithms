from string import ascii_lowercase

alphabets = ascii_lowercase
dict_alphabets = {}

index = 1
for alphabet in alphabets:
    dict_alphabets[alphabet] = str(index)
    index += 1

s = "iiii"
k = 2
# Expected Output: 6

s_num = ""
for i in s:
    s_num += dict_alphabets[i]


for i in range(k):
    s_num = sum(int(char) for char in s_num)
    s_num = str(s_num)
print(s_num)