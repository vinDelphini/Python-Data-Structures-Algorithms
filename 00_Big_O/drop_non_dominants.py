def print_numbers(n):

    numbers = []
    for i in range(n):
        for j in range(n):              # O(n2)
            numbers.append([i, j])

    k_numbers = []
    for k in range(n):                  # O(n)
        k_numbers.append(k) 
    
    return [numbers, k_numbers]


if __name__=="__main__":

    nums = print_numbers(10)

    for i in nums[0]:
        print(i[0], i[1])
    for j in nums[1]:
        print(j)
        

# the function has O(n2) & O(n), due to O(n) is negligible
# compared to O(n), we are gonna clasify it as O(n)
