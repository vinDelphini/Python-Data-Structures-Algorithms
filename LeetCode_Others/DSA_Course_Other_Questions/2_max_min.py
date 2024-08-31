def find_max_min(myList):
    max_num = min_num = myList[0]
    for num in myList:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return (max_num, min_num)

print(find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""