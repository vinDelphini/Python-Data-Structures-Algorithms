num1 = 11
num2 = num1         # num2 points to same location in memory

print(num1)
print(num2, "# num2 points to same location in memory")
print(id(num1))
print(id(num2))


num2 = 22
print("after updating")
print(id(num1))
print(id(num2))


# Dictionary 
print("\n Dictionary:")

dict1 = {'val': 11}
dict2 = dict1

print(dict1, dict2)

print(id(dict1))
print(id(dict2))

print("\n after updating:")

dict2['val'] = 22   

print(dict1, dict2, "# unlike integers value changed for dict1 when dict2 is updated but memory location doesn't change")
print(id(dict1))
print(id(dict2))

print("\n '{'val': 11}' python will remove this through a process called garbage collection")
