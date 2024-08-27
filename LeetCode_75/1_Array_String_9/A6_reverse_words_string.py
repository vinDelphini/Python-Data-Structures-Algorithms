t = "   a good   example   "
# lst = []
# pl = ""
# for i in t:
#     if i != " ":
#         pl += i
#     else:
#         lst.append(pl)
#         pl = ""
# lst.append(pl)

# s = list(filter(lambda x: x != "", lst))
# print(s)
# l, r = 0, len(s) -1
# while l < r:
#     s[l], s[r] = s[r], s[l]
#     l, r = l + 1, r - 1

# print(" ".join(s))

t = t.strip().split()
t.reverse()
print(" ".join(t))
