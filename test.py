nested_list = [3, [1, 2, 4], [5, [6, 7], 8], 9, [10, [11, [12, 13], 14], 15], 16, [17, 18], 19, [20]]
nested_list_reversed = list(reversed(nested_list))
print(nested_list_reversed)

for stack in nested_list_reversed:
    stack = nested_list_reversed.pop()
    print(stack)
