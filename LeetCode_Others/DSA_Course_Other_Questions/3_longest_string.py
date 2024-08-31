def find_longest_string(myLst):
    longest_word = ""
    for word in myLst:
        if len(word) > len(longest_word) :
            longest_word = word
    return longest_word


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""