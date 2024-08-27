def print_items(n):
    set_numbers = []
    for i in range(n):
        for j in range(n):
            set_numbers.append([i, j])
    return set_numbers


if __name__=="__main__":

    set_numbers = print_items(10)

    for numbers in set_numbers:
        print(numbers[0], numbers[1])
