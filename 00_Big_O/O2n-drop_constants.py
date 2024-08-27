def print_numbers_twice(n):

    numbers = []

    for i in range(n):
        numbers.append(i)
    
    for j in range(n):
        numbers.append(j)
    
    return numbers


if __name__=="__main__":

    numbers = print_numbers_twice(10)
    for number in numbers:
        print(number)


# O(2n) Order of 2n, since 2 is constant, we drop it, 
# therefore it is order of n O(n)
