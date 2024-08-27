# inefficient way - O(n2)
def item_in_common(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return i
    return False


list_1 = [1, 3, 5]
list_2 = [2, 4, 6]
# print(item_in_common(list_1, list_2))


# Efficient way - O(n)
def item_in_common_dict(lst1, lst2):
    dict_ = {}
    for i in list_1:
        dict_[i] = True
    for j in list_2:
        if j in dict_.keys():
            return dict_[j]
    return False


# print(item_in_common_dict(list_1, list_2))


def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


nums = [1,2,3,4,5,1,2]
dict_ = {}
for i in nums:
    if i in dict_.keys():
        dict_[i] = dict_.get(i, 0) + 1
    else:
        dict_[i] = 1
out = []
for key, value in dict_.items():
    if value == 1:
       out.append(key)

# print(out)


def first_non_repeating_char(string_):
    dict_ = {}
    for i in string_:
        if i in dict_.keys():
            dict_[i] = dict_.get(i, 0) + 1
        else:
            dict_[i] = 1
    for i in string_:
        if dict_[i] == 1:
            return i
    return None

# print(first_non_repeating_char('alphabet'))
# print(first_non_repeating_char('hello'))
# print(first_non_repeating_char('aabbcc'))


def group_anagrams(strings):

    dict_2 = {}
    for i in strings:
        sorted_i = ''.join(sorted(i))
        if sorted_i in dict_2:
            dict_2[sorted_i].append(i)
        else:
            dict_2[sorted_i] = [i]
    lst_1 = []
    for j in dict_2.values():
        lst_1.append(j)
    return lst_1


# print("1st set:")
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
#
# print("\n2nd set:")
# print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))
#
# print("\n3rd set:")
# print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


# print(two_sum([5, 1, 7, 2, 9, 3], 10))
# print(two_sum([4, 2, 11, 7, 6, 3], 9))
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
# print(two_sum([1, 3, 5, 7, 9], 10))
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )
# print ( two_sum([], 0) )

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9

my_set = set()
my_set.add(6)
my_set.update([2,3,6])
my_set.remove(3)
# print(my_set)
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
# print(union_set)

# Intersection of two sets
intersection_set = my_set.intersection(other_set)
# print(intersection_set)

# Difference between two sets
difference_set = my_set.difference(other_set)
# print(difference_set)

# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")

from collections import Counter
def remove_duplicates(my_list):
    # seen = set()
    # return [i for i in my_list if not (i in seen or seen.add(i))]
    return list({x: None for x in my_list}.keys())
    # return list(Counter(my_list).keys())


def unique_only(my_list):
    dict_ = {}
    for i in my_list:
        dict_[i] = dict_.get(i, 0) + 1
    return [key for key, value in dict_.items() if value == 1]


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]

new_list = remove_duplicates(my_list)
# print(new_list)
unique = unique_only(my_list)
# print(unique)
# list comprehension


def type(x, y=[]):
    y.append(x)
    return y

# print(type(1))
# print(type(2))


def has_unique_chars(string_):
    seen = set()
    for char in string_:
        if char in seen:
            return False
        seen.add(char)
    return True


# print(has_unique_chars('hello'))


def find_pairs(arr1, arr2, target):
    for i in arr1:
        for j in arr2:
            if i + j == target:
                print([i, j])


def find_pairs(arr1, arr2, target):
    out = []
    for num in arr2:
        compliment = target - num
        if compliment in arr1:
            out.append((compliment, num))
    return out

def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
# print(find_pairs(arr1, arr2, target))

n = "1001010010001"
# print(len(max(n.split('1'))))
counter = []
count = 0
for i in n:
    if i == '0':
        count += 1
    else:
        counter.append(count)
        count = 0
# print(max(counter))


def longest_consecutive_sequence(nums):
    numz = set(nums)
    nums = sorted(nums)
    length = []
    counter = 1
    longest_sequence = 0
    for i in nums:
        if i + 1 in numz:
            counter += 1
        else:
            length.append(counter)
            counter = 1
    return max(longest_sequence, max(length))


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))
